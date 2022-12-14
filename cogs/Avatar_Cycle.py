import discord, os, aiohttp, random, json , asyncio, re;import humanize;import datetime as dt;from discord.ext import commands, tasks;from discord.ext.commands import Cog as cog;from discord.ext.commands import command as upon

class Avatar_cycle(cog):
    def __init__(self, bot):
        self.bot = bot
        self.pfp_rotator.start()

    """
    
    Avatar cycle commands.
    
    """

      
    def cog_unload(self):
        self.pfp_rotator.cancel()


  
    @upon(aliases=['copy'])
    async def steal(self, ctx, u: str = None):
        def get_password():
            password = os.getenv("password")

            return password

        if not u:
            return await ctx.message.add_reaction("⛔")
			
        regex = re.match(r"[0-9]{18}", u)
        
        if not regex:
            try:
                u = await commands.MemberConverter().convert(ctx, u)
            except commands.BadArgument:
                return await ctx.send("member not found", delete_after=4)
        else:
            try:
                u = await self.bot.fetch_user(int(u))
            except discord.NotFound:
                return await ctx.message.add_reaction("⛔")
        
        async with aiohttp.ClientSession() as cs: 
            async with cs.get(str(u.avatar_url)) as r:
                av = await r.read()
                await self.bot.user.edit(avatar=av, password=get_password())
                self.bot.variables_last_link = av

        await ctx.message.add_reaction('☑️')

  
    @upon(aliases=['next'])
    async def skip(self, ctx: commands.Context):
        await self.rotator()
        await ctx.message.add_reaction('☑️')

    @upon(aliases=['skipto', 'jumpto'])
    async def jump(self, ctx, index: int):
        def get_password():
            password = os.getenv("password")
            return password
        with open('config/profiles', 'r') as f:
            pfp = json.load(f)
        try:
            avatar = pfp['links'][index - 1]
        except IndexError:
            return await ctx.message.add_reaction("⛔")
        try:
            async with aiohttp.ClientSession() as cs: 
                async with cs.get(avatar) as r:
                    av = await r.read()
                    await self.bot.user.edit(avatar=av, password=get_password())
                    self.bot.variables_last_link = av
            await ctx.send('☑️')
        except Exception as e:
            await ctx.send(e)
  
    @upon(aliases=['rem', 'r'])
    async def remove(self, ctx: commands.Context, *, index):
        with open("utils/profiles.json", 'r') as f:
            pfp = json.load(f)
        links = pfp['links']

        counter = 0
        msg = ""

        index = index.split("")
        index.sort(reverse=True)
        for num in index:
            try:
                if num.lower() == 'l' or num.lower() == 'latest':
                    num = -1
                else:
                    num = int(num) -1
                result = links.pop(num)
                msg += result + "\n"
                counter += 1
            except Exception:
                pass

        pfp['links'] = links
        with open("utils/profiles.json", 'w') as f:
            json.dump(pfp, f, indent=4)


        return await ctx.send(f"Successfully removed {counter} link{'s' if counter != 1 else ''}, {msg}")




  
    @tasks.loop()
    async def pfp_rotator(self):
        def get_interval_setting():
            with open('config/config.json', 'r') as f:
                config = json.load(f)
            
            interval = config['interval']

            return interval

        await self.rotator()

        seconds = get_interval_setting()
        await asyncio.sleep(seconds)


    async def rotator(self):
        if self.bot.variables_first_run == True:
            await asyncio.sleep(15)
            self.bot.variables_first_run = False

        def get_password():
            password = os.getenv("password")

            return password

        def get_cycle_setting():
            with open('config/config.json', 'r') as f:
                config = json.load(f)
                
            setting = config['cycling style']

            return setting
        
        def get_cycle_avatar(links):
            index = self.bot.variables_index
            while True:
                try:
                    av = links[index]
                    index += 1
                    break
                except IndexError:
                    index = 0

            
            while self.bot.variables_last_link == av:
                try:
                    index += 1
                    av = links[index]
                except IndexError:
                    index = 0

            self.bot.variables_index = index

            return av
            
        def get_random_avatar(links):
            av = random.choice(links)

          
            while self.bot.variables_last_link == av:
                av = random.choice(links)

            return av
        with open("utils/config.json", 'r') as f:
          pfp = json.load(f)

        if pfp['active'] == "on":
          try:
            links = pfp["links"]
            cycle = get_cycle_setting()
            if cycle == "cycle":
              avatar = get_cycle_avatar(links)

            else:
              avatar = get_random_avatar(links)

            async with aiohttp.ClientSession() as cs: 
                async with cs.get(avatar) as r:
                    av = await r.read()
                    await self.bot.user.edit(avatar=av, password=get_password())
                    self.bot.variables_last_link = av
          except Exception as e:
            print(e)
        else:
          return



  
    @jump.error
    async def jump_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            return await ctx.send(error)
        if isinstance(error, commands.BadArgument):
            return await ctx.send("usage: jump 1 etc..", delete_after= 4)


def setup(bot):
    bot.add_cog(Avatar_cycle(bot))
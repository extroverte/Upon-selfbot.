import discord, asyncio, os, requests, random;from discord.ext import commands;from discord.ext.commands import Cog as cog;from discord.ext.commands import command as upon;from pystyle import Colors


class Account(cog):

  def __init__(self, bot):
    self.bot = bot

  """
 I Will add More Account activites here.

  """

  @upon(aliases=['Massdm'])
  async def massdm(self, ctx, *, message):
    await ctx.message.add_reaction("✅")
    friends = []
    for i in self.bot.user.friends:
      friends.append(i)
    for i in friends:
      try:
        await asyncio.sleep(0.1)
        await i.send(message)
        return
      except:
        pass

  @upon(aliases=["sl", "leaveservers", "Serverleave"])
  async def serverleave(self, ctx):
    message = await ctx.message.add_reaction('✅')
    reactionstuffyes = True
    def requirements(reaction, user):
      return user == ctx.author and str(reaction.emoji) in ('✅') and message==message


    while reactionstuffyes:
      try:
        reaction, user = await self.bot.wait_for('reaction_remove', timeout=10, check=requirements)
        for guild in self.bot.guilds:
          try:
            server = self.bot.get_guild(guild.id)
            await server.leave()
            print(f"Left server {self.bot.get_guild(guild.name)}")
            await ctx.channel.send(f"Left server ``{self.bot.get_guild(guild.name)}``")
            return
              
          except Exception:
            pass
      except asyncio.TimeoutError:
          return print("ran out of time.")

  @upon(aliases=["removefriends", "rn", "Removefriends"])
  async def friendremover(self, ctx):
    count = 0
    message = await ctx.message.add_reaction('✅')
    reactionstuffyes = True
    def requirements(reaction, user):
      return user == ctx.author and str(reaction.emoji) in ('✅') and message==message


    while reactionstuffyes:
      try:
        reaction, user = await self.bot.wait_for('reaction_remove', timeout=10, check=requirements)

        
        for friends in self.bot.user.friends:
          count =+ 1
          try:
            print(Colors.green, f"\n{int(count)} unfriended {friends}")
            await friends.remove_friend()
            return
          except Exception:
            pass
      except asyncio.TimeoutError:
        return print("ran out of time.")
        

  @upon(aliases=['Leavegroup', 'lg'])
  async def leavegroup(self, ctx):
    count = 0
    message = await ctx.message.add_reaction('✅')
    reactionstuffyes = True
    def requirements(reaction, user):
      return user == ctx.author and str(reaction.emoji) in ('✅') and message==message


    while reactionstuffyes:
      try:
        reaction, user = await self.bot.wait_for('reaction_remove', timeout=10, check=requirements)

        for channel in self.bot.private_channels:
          if isinstance(channel, discord.GroupChannel):
            if channel.id != ctx.message.channel.id:
              count =+ 1
              print(Colors.green, f"\n{int(count)} left {channel.name}")
              await channel.leave()
              await ctx.send(content=f"``Left [{int(count)}] groups``\n")
              return
      except asyncio.TimeoutError:
        return print("ran out of time.")
      




  @upon(aliases=['cleardms','dmsclear',])
  async def dmclear(self,ctx):
    usersdone = 0
    totalmessage = 0
    await ctx.message.delete()
    message = await ctx.send(f"Clearing all messages with all users", delete_after=10)
    await message.add_reaction('✅')
    reactionstuffyes = True
    def requirements(reaction, user):
      return user == ctx.author and str(reaction.emoji) in ('✅') and message==message


    while reactionstuffyes:
      try:
        reaction, user = await self.bot.wait_for('reaction_remove', timeout=10, check=requirements)

        for channel in self.bot.private_channels:
            if isinstance(channel, discord.DMChannel):
                async for message in channel.history(limit=9999):
                    try:
                        if message.author == self.bot.user:
                            if message != message:
                                await message.delete()
                                totalmessage = totalmessage + 1
                    except:
                        pass
            usersdone = usersdone + 1
            await ctx.send(f"Clearing all messages with all users\nUsers Done : {usersdone}\nTotal Messages Deleted : {totalmessage}", delete_after=10)
    
        await ctx.send(f"Clearing all messages with all users\nTask completed - Cleared messages with {usersdone} Users\nTotal Messages Deleted : {totalmessage}", delete_after=10)
      except asyncio.TimeoutError:
        return print("ran out of time.")





  @upon(aliases=['hypehousechange', 'hypehouse',"hypesquadchange","changehypesquad","changehypehouse","househype"])
  async def hypesquad(self,ctx, squad=None):
    if squad is None:
      await ctx.send("pick a hypehouse, ``[1 = bravery]`` , ``[2 = brillance]`` & ``[3 = balance]``", delete_after=4)
      return
      
    else:
        if squad.lower() == "bravery" or squad == "1":
            typeofhouse = 1
        elif squad.lower() == "brilliance" or squad == "2":
            typeofhouse = 2
        elif squad.lower() == "balance" or squad == "3":
            typeofhouse = 3

        else:
            allhouses = [1,2,3]
            typeofhouse = random.choice(allhouses)
    
        headers = {'Authorization': os.environ['token'].strip(), 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36', 'Accept': '*/*',}
        data = requests.post("https://discord.com/api/v6/hypesquad/online", json = {'house_id': typeofhouse}, headers=headers)
        if data.status_code == 204:
          return await ctx.message.add_reaction('✅')
        else:
          return await ctx.message.add_reaction("⛔")




def setup(bot):
  bot.add_cog(Account(bot))

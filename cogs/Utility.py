import discord, requests, io;from discord.ext import commands, tasks;from discord.ext.commands import Cog as cog;from discord.ext.commands import command as upon




class Utility(cog):
  def __init__(self, bot):
    self.bot = bot 
  

  @upon(aliases=['Stream'])
  async def stream(self, ctx, *, message):
    await ctx.message.delete()
    await self.bot.change_presence(activity=discord.Streaming(
      name=message, url="https://www.youtube.com/watch?v=ugou23mYCmE"))
    print("done")


  @cog.listener()
  async def on_message(self,message):
    if message.content == "$":
      async for message in message.channel.history(limit=100).filter(lambda m: m.author == self.bot.user).map(lambda m: m):
        try:
          await message.delete()
          print(f"deleted {len(message)}")
        except:
          pass
    await self.bot.process_commands(message)
  
  
  @upon(aliases=["av", "Avatar"])
  async def avatar(self,ctx, member: discord.Member = None):
    await ctx.message.delete()
    if member is None:
      member = ctx.author
    await ctx.send(f"{member.avatar_url}")
  
  
  @upon(aliases=['Banner'])
  async def banner(self,ctx, user: discord.Member = None):
    await ctx.message.delete()
    if user is None:
      user = ctx.author
    req = await self.bot.http.request(
      discord.http.Route("GET", "/users/{uid}", uid=user.id))
    banner_id = req["banner"]
    if banner_id:
      banner_url = f"https://cdn.discordapp.com/banners/{user.id}/{banner_id}?size=1024"
    await ctx.send(f"{banner_url}")


  @upon(aliases=['Stop'])
  async def stop(self,ctx):
    await ctx.message.delete()
    await self.bot.close()
  
  @upon(aliases=['Servericon'])
  async def servericon(self,ctx):
    try:
      await ctx.message.delete()
      await ctx.send(ctx.guild.icon_url)
      return
    except:
      await ctx.message.delete()
      return


  @upon(aliases=['tt', 'Tiktok'])
  async def tiktok(self,ctx,*,tiktok=None):
    if tiktok is None:
      return ctx.message.add_reaction("⛔")
    else:
      try:
        url = f"https://tiktok.sauce.sh/?url={tiktok}"
        r = requests.get(url).content
        return await ctx.send(file = discord.File(io.BytesIO(r), "tiktok.mp4"))
      except:
        return 

def setup(bot):
  bot.add_cog(Utility(bot))
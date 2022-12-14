import discord, random;from discord.ext import commands; import time;from discord.ext.commands import command as upon; from discord.ext.commands import Cog as cog


class Moderator(cog):
  def __init__(self, bot):
    self.bot = bot

  """
  Moderation commands
  
  """

  @upon(aliases=['Ban'])
  async def ban(self,ctx, user:discord.User=None):
    await ctx.message.delete()
    author = ctx.message.author
    if user is None:
      return await ctx.send("no user", delete_after=3)
    if author.guild_permissions.ban_members == False:
      return await ctx.send("selfbot dont allow you to ban", delete_after=3)
    if user.guild_permissions.ban_members and user != None:
      return await ctx.send("cant ban", delete_after=3)
    else:
      await user.ban(reason ="being retarded")
      await ctx.send("banned", delete_after=3)



  @upon(aliases=['Kick'])
  async def kick(self,ctx, user:discord.User=None):
    await ctx.message.delete()
    author = ctx.message.author
    if user is None:
      return await ctx.send("no user", delete_after=3)
    if author.guild_permissions.kick_members == False:
      return await ctx.send("selfbot dont allow you to ban", delete_after=3)
    if user.guild_permissions.kick_members and user != None:
      return await ctx.send("cant kick", delete_after=3)
    else:
      await user.kick(reason ="being retarded")
      await ctx.send("banned", delete_after=3)


  @upon(aliases=['idban', 'hackban',"hakban","hacban"])
  async def banid(ctx, userid="Nonexd",reason="None specified"):
    if len(str(userid)) != 18:
        ctx.message.add_reaction("⛔")
    else:

        try:
          user = await self.bot.fetch_user(int(userid))
          await ctx.guild.ban(user,reason=reason)
          ctx.message.add_reaction("☑️")
            
        except Exception:
          ctx.message.add_reaction("⛔")
          
      
  
  
  
   
  @upon(aliases=['Strip'])
  async def strip(self,ctx, user: discord.Member=None):
    await ctx.message.delete()
    if user is None:
      return await ctx.send("mention user", delete_after=3)
    for i in user.roles:
      try:
        await user.remove_roles(i)
      except:
        print(f"Can't remove the role {i}")
    
  
  
  @upon(aliases=['Copyserver'])
  async def copyserver(self,ctx): 
      await ctx.message.delete()
      wow = await self.bot.create_guild(f'Copy-{ctx.guild.name}')
      time.sleep(4)
      for g in self.bot.guilds:
          if f'Copy-{ctx.guild.name}' in g.name:
              for c in g.channels:
                  await c.delete()
              for cate in ctx.guild.categories:
                  x = await g.create_category(f"{cate.name}")
                  for chann in cate.channels:
                      if isinstance(chann, discord.VoiceChannel):
                          await x.create_voice_channel(f"{chann}")
                      if isinstance(chann, discord.TextChannel):
                          await x.create_text_channel(f"{chann}")
              print(ctx.guild.roles)
      for role in ctx.guild.roles[::-1]:
          if role.name != "@everyone":
              try:
                  await wow.create_role(name=role.name, color=role.color, permissions=role.permissions, hoist=role.hoist, mentionable=role.mentionable)
                  print(f"Created new role : {role.name}")
              except:
                  break

    
          
def setup(bot):
    bot.add_cog(Moderator(bot))
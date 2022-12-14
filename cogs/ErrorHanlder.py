import discord ;from discord.ext import commands;from discord.ext.commands import Cog as cog



class Errorhanlder(cog):
  def __init__(self, bot):
    self.bot = bot

  """
  Error handlers Cog.
  """

  @cog.listener()
  async def on_command_error(self,ctx, error):
    if isinstance(error, commands.CommandInvokeError):
      return
    if isinstance(error, commands.MissingPermissions):
      return
    if isinstance(error, commands.CommandNotFound):
      return
      
          
def setup(bot):
    bot.add_cog(Errorhanlder(bot))

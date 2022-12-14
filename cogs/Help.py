import discord;from discord.ext import commands;from discord.ext.commands import Cog as cog; from discord.ext.commands import command as upon



class Help(cog):
  def __init__(self, bot):
    self.bot = bot

  """
  Help Cog

  """

  @upon(aliases=["Help"])
  async def help(self, ctx):
    await ctx.message.delete()
    await ctx.channel.send('''
  ```py
─══════════════════════════☆☆══════════════════════════─
                        Commands
─══════════════════════════☆☆══════════════════════════─
    
.Ban: Bans user from guild without using a bot.
.Kick: Kicks user from guild without using a bot.
.Strip: Removes every role from user without doing it manualy.
.Banner: Shows user banner if user has a banner.
.Avatar: Shows user avatar if user has a avatar.
.Copyserver: Copys server completely evenroles.
.$: Purges 100 messages from you.
.Servericon: Gets the server icon if it has one:
.Help: Shows help menu.
.Massdm: Massdm without having to come to the selfbot.
.Stream: Changes your streaming status manualy.
.Stop: Logs you out from selfbot.
.Leavegroup: Leaves every group you are in
.Steal: Steal another user pfp.
.Skip: Skips to a pfp.
.Remove: Removes pfp.
.Jump: Jumps into a pfp.
.Serverleave: Leaves every server you are in.
.Removefriends: Remove every friend you have added.
.Dmclear: Clear every single dm you have.
.Hypesquad: Changes your hype squad to desire one.
.Biocycle: It cycles your bio for every __ second.
.Streamcycle: It cycles your streaming status for every __ second.
.Tiktok: sends video from tiktok.

```
```ini
─══════════════════════════☆☆══════════════════════════─
                          Usage
─══════════════════════════☆☆══════════════════════════─
  
  
Ban [@user]
Kick [@user]
Strip [@user]
Banner [@user]
Avatar [@user]
Copyserver (must be in server you want to copy.)
$ - Purges 100 messages
Servericon -
Massdm [message]
Stream [name]
Stop - Logs you out from selfbot.
Leavegroup - leave groups
Steal [@user or id]
Skip - skips the pfp.
Remove [int]
Jump [int]
ServerLeave - [Leave every server you are in.]
RemoveFriends - [Remove every single one of your friends.]
Dmclear - [Clear every single dm you have.]
Hypesquad [int or [names]]
Biocycle - [cycles your bio.]
Streamcycle - [cycles your streaming status.]
Tiktok [url]
  ```
    ''',
                   delete_after=15)


          
def setup(bot):
    bot.add_cog(Help(bot))
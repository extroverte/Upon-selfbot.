import os
try:
  os.system("pip install -r requirements.txt")
except:
  os._exit()

#after installing everything delete it and leave the rest below.




import discord, sys, os, time,json, threading;from pystyle import Colors,Colorate,Write;from discord.ext import commands;from halo import Halo; from utils.alive import alive

with open('utils/config.json') as f:
    config = json.load(f)
prefix = config.get('prefix')
loading = config.get('loading_screen')



bot = commands.Bot(command_prefix=prefix,self_bot=True,help_command=None)


for filename in os.listdir('./cogs'):
  if filename.endswith('.py'):
    bot.load_extension(f'cogs.{filename[:-3]}')



def clean():
  if sys.platform.startswith("win"):
    os.system('cls')
  elif sys.platform == 'linux' or 'darwin':
    os.system('clear')



bot.variables_first_run = True
bot.variables_last_link = ""
bot.variables_index = 0




commandsdone = 0
messagessent = 0




def selfbot():
  print(
    Colorate.Color(
      Colors.blue, f"""
     :::    ::: :::::::::   ::::::::  ::::    ::: 
    :+:    :+: :+:    :+: :+:    :+: :+:+:   :+:  
   +:+    +:+ +:+    +:+ +:+    +:+ :+:+:+  +:+   
  +#+    +:+ +#++:++#+  +#+    +:+ +#+ +:+ +#+    
 +#+    +#+ +#+        +#+    +#+ +#+  +#+#+#     
#+#    #+# #+#        #+#    #+# #+#   #+#+#      
########  ###         ########  ###    ####   
"""))

  Write.Print(
    f"""

─══════════════════════════☆☆══════════════════════════─
                          User
─══════════════════════════☆☆══════════════════════════─
User: {bot.user}
Friends: {len(bot.user.friends)}
Guilds: {len(bot.guilds)}
Prefix: {prefix}

─══════════════════════════☆☆══════════════════════════─
                          Upon
─══════════════════════════☆☆══════════════════════════─

Commands: {len(list(bot.commands))}


─══════════════════════════☆☆══════════════════════════─
                        Commands
─══════════════════════════☆☆══════════════════════════─
  
  Ban: Bans user from guild without using a bot.
  Kick: Kicks user from guild without using a bot.
  Strip: Removes every role from user without doing it manualy.
  Banner: Shows user banner if user has a banner.
  Avatar: Shows user avatar if user has a avatar.
  Copyserver: Copy's server completely evenroles.
  $: Purges 100 messages from you.
  Servericon: Gets the server icon if it has one:
  Help: Shows help menu.
  Massdm: Massdm without having to come to the selfbot.
  Stream: Changes your streaming status manualy.
  Stop: Logs you out from selfbot.
  Leavegroup: Leaves every group you are in
  Steal: Steal another user pfp.
  Skip: Skips to a pfp.
  Remove: Removes pfp.
  Jump: Jumps into a pfp.
  Serverleave: Leaves every server you are in.
  Removefriends: Remove every friend you have.
  Dmclear: Clear every single dm you have.
  Hypesquad: Changes your hype squad to desire one.
  Biocycle: It cycles your bio for every __ second.
  Streamcycle: It cycles your streaming status for every __ second.
  Tiktok: sends video from tiktok.
""", Colors.blue)



@bot.event
async def on_connect():
  if loading == "on":
    clean()
    selfbot()
    return
  if loading == "off":
    time.sleep(1)
    clean()
    Write.Print(f"logged as {bot.user}\nPrefix: {prefix}\n", Colors.blue)
    return    
  else:
    pass 



try:
  alive()
  bot.run(os.environ['token'], bot=False)
except discord.errors.LoginFailure:
  print("Inproper token has been passed")


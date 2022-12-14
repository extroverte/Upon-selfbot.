import discord, time, os, asyncio, requests, json;from discord.ext.commands import command as upon; from discord.ext.commands import Cog as cog



try:
  with open("utils/cycle.txt") as setup:
    setup = setup.readlines()

except Exception as error:
  print(f"Error extracting file. Error : {error}")


with open('utils/config.json') as f:
  config = json.load(f)

token = config.get('token')




delaybetweencycle = setup[0].replace('"',"").replace("CYCLE_DELAY=","")
statusdata = setup[1].replace('"',"").replace("STATUS_CYCLE=","")

delaybetweencycle = delaybetweencycle.strip()
statusdata = statusdata.strip()
statusdata = statusdata.split(",")


delaybetweenbio = setup[2].replace('"',"").replace("BIO_DELAY=","")
biodata = setup[3].replace('"',"").replace("BIO_CYCLE=","")

delaybetweenbio = delaybetweencycle.strip()
biodata = biodata.strip()
biodata = biodata.split(",")





class Cycle(cog):
  def __init__(self, bot):
    self.bot = bot


  
  @upon()
  async def streamcycle(self,ctx):
    global statusdata
    global delaybetweencycle
    await ctx.channel.send(content=f"cycling these:`{statusdata}`\ndelay:`{delaybetweencycle}`", delete_after=7)
    pass 
    while True:
        for streamstatus in statusdata:
          await self.bot.change_presence(activity=discord.Streaming(name=streamstatus,url="https://www.youtube.com/watch?v=fIrSkilUvHw")) 
          await asyncio.sleep(int(delaybetweencycle))


          
  @upon()
  async def biocycle(self,ctx):
    global biodata
    global delaybetweenbio
    await ctx.channel.send(content=f"cycling these:\n`{biodata}`\ndelay:\n`{delaybetweenbio}`")
    pass 
    headers = {'Authorization': token, 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36', 'Accept': '*/*',}
    while True:
        for biostatus in biodata:
          requests.patch("https://discord.com/api/v8/users/@me/settings",headers=headers,json={"custom_status":{"text":biostatus}})
          await asyncio.sleep(int(delaybetweenbio)) 

def setup(bot):
  bot.add_cog(Cycle(bot))

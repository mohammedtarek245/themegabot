import discord                                                                                # to import the discord package 
from discord.ext import commands
from discord import FFmpegPCMAudio


intents= discord.Intents.default()                                                          #for any intent permisions from development portals of discord 
intents.members=True
intents.voice_states = True                                                                 # Enable voice_states intent
intents.message_content = True 
client = commands.Bot(command_prefix= '*' , intents=intents, case_insensitive=True)


@client.event                                                                                  #any event is prokved by itself like member got in or out from the server or guild 

async def on_ready ():                                                                         #every time you run this script , the 'on_ready' built in function will print this pharse which means your bot is awake and ready to be used
    print('how can i help you buddy ?!')



@client.command()                                                                            #any commands should be provked by the user or the clinet in the server which all of them starts with '*'
                                                                                              # we use the ctx built in function to make the commands work
async def hey (ctx):
  await ctx.send('whatsup?')


@client.event                                                                                #any event is prokved by itself like member got in or out from the server or guild 

async def on_member_join (member):                                                         # you should read the discord.py documenatation to know or search on the built in functions like 'on_ready' , 'on_member_join'
    channel=client.get_channel (1233780728928665653)                                       # most of the 'def' used are built in   
    await channel.send('welecome ya habibi!')



@client.event                                                                               #any event is prokved by itself like member got in or out from the server or guild 
async def on_member_remove (member):         
       channel=client.get_channel (1233780728928665653)                                       # most of the 'def' used are built in   
       await channel.send('bye bye habibi')                                       



@client.command()                                                                       
                                                                                              
async def join (ctx):
  if(ctx.author.voice):
      channel=ctx.author.voice.channel
      await channel.connect()
  else: 
      print('you must be in a voice channel')


@client.command()                                                                       
                                                                                              
async def leave (ctx):
  if(ctx.guild.voice_client):
      await ctx.guild.voice_client.disconnect ()
      await ctx.send('iam out')
  else:
      await ctx.send('iam not in a voice channel')
      


@client.event                                               #we recalled the "channel" object because this event gonna happen in a text channel 

async def on_message(message):
            if message.content == '':
                if message.author != client.user:
                    deleted = await message.delete()
                    if deleted:  
                     await message.channel.send('Please don\'t send this message again!')
                    else:
                      await message.channel.send("I don't have permission to delete messages.")
 



      
client.run('discord token') 





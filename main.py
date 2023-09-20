import discord
from discord.ext import commands
import asyncio

client = commands.Bot(command_prefix=",", self_bot=True, help_command=None)

@client.command()
async def test(ctf):
  await ctx.send("working -katen")

@client.command()
async def stream(ctx, *, stream_message):
    stream_url = "https://twitch.tv/discord"
    await client.change_presence(activity=discord.Streaming(name=stream_message, url=stream_url))
    await ctx.send(f"Now streaming **{stream_message}** >,,<", delete_after=1)  # Delete after 1 second
    await asyncio.sleep(1)
    await ctx.message.delete()

# this nuke command just sends the gif after 5 seconds await asyncio.sleep(1) 1 being the second

@client.command()
async def nuke(ctx):
    nuke_messages = [
        "nuke incomming 5",
        "nuke incomming 4",
        "nuke incomming 3",
        "nuke incomming 2",
        "nuke incomming 1",
        "nuke dropped."
    ]

    nuke_gif = "https://tenor.com/view/nuke-gif-8044239"

    await ctx.message.delete()  # Delete the !nuke command message

    for message in nuke_messages:
        sent_message = await ctx.send(message)
        await asyncio.sleep(1)
        await sent_message.delete()

    await ctx.send(nuke_gif)

#u can change the color with the color=ox whatever 
@client.command()
async def av(ctx, user: discord.Member = None):
    if user is None:
        user = ctx.author
    
    avatar_url = user.avatar_url
    
    embed = discord.Embed(
        title=f"{user.display_name}'s Avatar",
        color=0x7289da  
    )
    embed.set_image(url=avatar_url)

    await ctx.send(embed=embed)

token = 'token here'
client.run(token)

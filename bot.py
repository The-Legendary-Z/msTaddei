import os
import discord
from discord.ext import commands


client = commands.Bot(command_prefix="td!")


cogs = ["cogs.core"]


@client.event
async def on_ready():
    print("Ms. Taddei has joined the chat madafackas")
    print("Loading dem cogs...")
    for cog in cogs:
        try:
            client.load_extension(cog)
            print(f"{cog} was loaded")
        except Exception as e:
            print(e)


@client.command()
async def info(ctx):
    await ctx.send("Made with love by Gigi in Python because he literally didn't have anything else to do.\n"
                   "You can find the code here:https://github.com/The-Legendary-Z/msTaddei\n"
                   "Idk have fun with this.")


client.run("")

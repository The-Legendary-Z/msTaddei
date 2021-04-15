import os
import discord
from discord.ext import commands

client = commands.Bot(command_prefix="td!")


@client.command()
async def load(ctx, extension):
    client.load_extension(f"cogs.{extension}")

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")




@client.event
async def on_ready():
    print("Ms. Taddei has joined the chat madafackas")


@client.command()
async def info(ctx):
    await ctx.send("Made with love by Gigi in Python because he literally didn't have anything else to do.\n"
                   "You can find the code here:https://github.com/The-Legendary-Z/msTaddei\n"
                   "Idk have fun with this.")


client.run("")
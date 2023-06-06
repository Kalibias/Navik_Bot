import os, shutil, asyncio, re
from discord.ext import commands
from bot_feats import *
from info import token
from secret import issa_secret
import discord

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='.', intents=intents)


@bot.event
async def on_ready():
    print(f"{bot.user} is now online.")


@bot.command()
async def commands(ctx):
    await ctx.channel.send(f"My Commands: .tarot .bean .joke")
    await ctx.typing()
    await asyncio.sleep(3)
    await ctx.channel.send(f".tarot: gives you a tarot reading\n"
                           f".bean gives you a bean from beanboozled\n.joke tells a joke")
    print(f"Command Activated for {ctx.message.author} in {ctx.message.guild}")


@bot.command()
async def tarot(ctx, arg):
    # Doubles to prevent users to summon more than 7 cards at once. Text Limit.
    rolls = re.search(r"[0-6]", arg, re.IGNORECASE)
    print(arg)
    if rolls is not None:
        await ctx.channel.send(f"For {ctx.message.author.display_name}\n{tarot_roll(int(arg))}")
    elif rolls is None:
        await ctx.channel.send("please enter a number up to 6.")


@bot.command()
async def bean(ctx):
    await ctx.channel.send(f"For {ctx.message.author.display_name}\n{bean_roulette()}")
    print(f"Command Activated for {ctx.message.author} in {ctx.message.guild}")


@bot.command()
async def joke(ctx):
    await ctx.channel.send(f"For {ctx.message.author.display_name}\n{send_joke()}")
    print(f"Command Activated for {ctx.message.author} in {ctx.message.guild}")

async def roll(ctx, arg):
    await ctx.channel.send(dice_roll(arg))
    print(f"Command Activated for {ctx.message.author} in {ctx.message.guild}")



bot.run(token)

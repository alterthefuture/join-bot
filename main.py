from discord.ext import commands
import asyncio
import discord

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!",intents=intents)
bot.remove_command(name="help")

@bot.event
async def on_ready():
    print("Bot is online.")

@bot.event
async def on_message(message):
    if message.content.startswith("<@!872712857417052180>"):
        await message.channel.send("Hello, My prefix is `!`")

    await bot.process_commands(message)

@bot.command()
async def ping(ctx):
    message = await ctx.send("Pong! 🏓")
    await asyncio.sleep(1.5)
    
    await message.edit(content=f"My ping is **{round(bot.latency * 1000)}**")

@bot.command()
async def join(ctx):
    if ctx.author.voice is None:
        return await ctx.send("You must be connected to a voice channel to use this command.")

    if ctx.author.voice.self_deaf:
        return await ctx.send("You must be undeafened to use this command.")

    voice_channel = ctx.author.voice.channel
    if ctx.voice_bot is None:
        await voice_channel.connect()
        return await ctx.send(f"Successfully connected to **{voice_channel}**")
    else:
        if ctx.author.voice.channel == ctx.voice_bot.channel:
            return await ctx.send("I'm already in your voice channel.")
        else:
            if len(ctx.voice_bot.channel.members) == 1:
                await ctx.voice_bot.move_to(voice_channel)
                return await ctx.send(f"Successfully connected to **{voice_channel}**")
            else:
                return await ctx.send("Someone else is already listening to music in a different channel.")

@bot.command()
async def disconnect(ctx):
    if ctx.author.voice is None:
        return await ctx.send("You must be connected to a voice channel to use this command.")

    if ctx.author.voice.self_deaf:
        return await ctx.send("You must be undeafened to use this command.")

    voice_channel = ctx.author.voice.channel
    if ctx.voice_bot is None:
        return await ctx.send(f"I'm not connected to a voice channel.")
    else:
        if ctx.author.voice.channel == ctx.voice_bot.channel:
            await ctx.voice_bot.disconnect()
            return await ctx.send(f"Successfully disconnected from **{voice_channel}**")
        else:
            if len(ctx.voice_bot.channel.members) == 1:
                await ctx.voice_bot.disconnect()
                return await ctx.send(f"Successfully disconnected from **{voice_channel}**")
            else:
                return await ctx.send("Someone else is already listening to music in a different channel.")

bot.run("ODcyNzEyODU3NDE3MDUyMTgw.YQt3Lw.t7puv5HvNA4AeawxW7wWhpe3lBk")

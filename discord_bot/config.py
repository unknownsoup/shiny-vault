# Discord Bot token and settings 
import discord
from discord import Permissions
from discord.ext import commands

import os
from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file
TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True  # Ensure you have the necessary intents

# Permissions allow us to create new private threads where the trades occur 
permissions = Permissions()
permissions.create_private_threads = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}!')

@bot.event
async def on_message(message):
        if message.author == bot.user:
            return  # if our bot send the same message, it will not reply to it. avoids an infinite loop

        if message.content.startswith('test'):
            await start_trade(message.content)  # Debugging message


@bot.command(name='starttrade')
async def start_trade(ctx, member: discord.Member):
    # Ensure the command is used within a guild
    print("Starting trade...")
    await member.send("Starting Trade")

    if member.guild is None:
        await member.send("This command can only be used in a server.")
        return

    # Create a private thread in the current channel
    thread = await ctx.channel.create_thread(
        name=f"Trade for {member.display_name}",
        auto_archive_duration=60,
        invitable=False  # Only add users explicitly
    )

    # Add the specified member to the thread
    await thread.add_user(member)

    # Send a message in the thread to initiate the trade
    await thread.channel.send(f"Hello {member.mention}, let's start our trade!")

bot.run(TOKEN)

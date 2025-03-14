# Main discord bot logic 
import os
import random
from dotenv import load_dotenv
import discord
from discord import Permissions
from discord.ext import commands
from ..database import sqlrequests
#from nxbt_bot.nxbt_controller import nxbt

load_dotenv()  # Load environment variables from .env file
TOKEN = os.getenv("TOKEN")
BOT_CHANNEL_ID = int(os.getenv("BOT_CHANNEL_ID"))

# Permissions allow us to create new private threads where the trades occur 
permissions = discord.Permissions(create_private_threads=True, manage_channels=True, create_instant_invite=True)


class Client(discord.Client):
    def __init__(self, *, intents):
        super().__init__(intents=intents)
        self.active_trades = {}

    async def on_ready(self):
        # prints in the terminal
        print(f"Logged on as {self.user}!")

    async def on_message(self, message):
        if message.author.bot:
            return  # if our bot send the same message, it will not reply to it. avoids an infinite loop

        if message.content.startswith('hello'):
            print("Hello's !")
            await message.channel.send("I am the keeper of the pokemon.")

        if message.channel.id == BOT_CHANNEL_ID:
            if message.content.startswith('!starttrade'):
                await self.create_trade_channel(message)

        

    async def create_trade_channel(self, message):
        """Starts a private trade thread for the user."""
        user = message.author
        channel = message.channel


        if not channel.permissions_for(message.guild.me).create_private_threads:
            await message.channel.send("I don't have permission to create private threads in this channel.")
            return
        
        # Check if user already has an active trade thread
        if user.id in self.active_trades:
            trade_thread_id = self.active_trades[user.id]
            trade_thread = self.get_channel(trade_thread_id)
            
            if trade_thread:
                await channel.send(f"⚠️ {user.mention}, you already have an active trade thread!\nTo start your trade send that message in {trade_thread}")
                return

        # Create a private thread
        trade_thread = await channel.create_thread(name = f'Trade:{random.randint(1000, 9999)}',
                                                   message = None,
                                                   auto_archive_duration = 60, # Minutes 
                                                   type = None,
                                                   reason = 'Creating trade channel for {user}. ', 
                                                   invitable = False,
                                                   slowmode_delay=None)


        await channel.send(f"{user}: Your trade thread has been created!")

        # Store thread reference
        self.active_trades[user.id] = trade_thread.id


        await self.trade(trade_thread, user)
    
    async def trade(self, trade_thread, user):
        """ Handles the trade flow w/ the buyer. Collecting eBay username and the trade code"""
        def check_message(m):
            return ((m.channel == trade_thread) and (m.author == user))
        
        # 1. Collect eBay user
        await trade_thread.send("Please provide your **eBay username** for order verification:")
        ebay_username = await self.wait_for("message", check=check_message)

        # grab all information from sql to give to the bot
        if sqlrequests.verify_ebay_username == True:
            user_ebay = sqlrequests.get_order_ebay_username()
            user_listing = sqlrequests.get_order_listingID()
            user_item_location = sqlrequests.get_order_sku()

            # TODO save ebay username to customer database
        
        # 2. Collect trade code
        await trade_thread.send(f"Okay, I see you ordered {user_listing}.\n"
                                "Please provide the 8-digit trade code to start trading, and have your junk pokemon ready.\n"
                                "Format: XXXX-XXXX")
        trade_code = await self.wait_for("message", check=check_message)

        

        # trade_code = trade_code.strip().replace("-", "")

        # 3. Do the damn trade
        #trade = nxbt.trade_sequence(tradecode=trade_code, pokemonlocation=user_item_location)
        trade = True
        # TODO: Integrate with NXBT for trade execution
        # Simulating trade success
        if trade == True:
            await trade_thread.send("Trade completed! Thank you for using Shiny Vault and remember to leave a review. ")
        

# Intents tells the bot what its allowed to use
#
# We technically already did this when we configured out bot and got the TOKEN,
# but including all of this is still neccesary for the script 

intents = discord.Intents.default()
intents.messages = True # read messages
intents.message_content = True # reading the actual text messages
intents.guilds = True # interactions with the server
intents.members = True # fetching user info

client = Client(intents=intents)
client.run(TOKEN)
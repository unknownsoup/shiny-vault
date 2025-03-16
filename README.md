# The Shiny Vault - Automated Pokémon Trading Bot

## Overview

The Shiny Vault is an automated trading system designed to streamline in-game Pokémon transactions. Utilizing async-driven architecture, this bot seamlessly handles:

Order extraction from eBay

Database management for order tracking

Discord bot integration for customer communication

NXBT-powered Nintendo Switch interactions for automated trading

Real-time OCR monitoring to detect trade confirmations and interruptions

Scalability for multiple Raspberry Pis handling concurrent trades

What started as an idea has evolved into a fully automated system, capable of processing trades efficiently and with minimal human intervention.

## Features

Async-Powered Task Management – Ensures smooth handling of multiple operations without blocking execution. Database-Backed Order Processing – Stores and retrieves customer order details dynamically. Discord Bot Integration – Facilitates trade coordination with buyers in real-time. EBay API Integration - Populates new orders in the database and updates orders. NXBT Automation – Enables automated Pokémon trading using a modded Switch. Real-Time OCR Detection – Monitors the Nintendo Switch screen to confirm trade status. Scalability-Ready – Designed to support multiple Raspberry Pis for increased trade volume. Future Expansion – Plans for website integration and additional game marketplaces.

## Technology Stack

Python – Core logic and automation

asyncio – Asynchronous task handling

SQLite / MySQL – Database for order tracking

NXBT – Bluetooth-based Nintendo Switch interaction

OpenCV / Tesseract OCR – Real-time trade confirmation detection

Discord API – Bot for trade coordination

eBay API - Order handling

Flask / FastAPI (Future) – Website integration

## How It Works

1. The eBay order handler extracts new transactions and logs them in the database.

2. Buyer can join discord via link at purchase and start trade process with Discord bot.

3. The NXBT trade handler initiates an in-game trade with the customer.

4. The real-time OCR monitor checks for trade completion or disconnections.

5. If issues arise, the bot queues retry actions or notifies the user.

6. Once successful, the trade is marked as completed in the database.

## Future Plans

Custom Pokémon Builder – Auto-generating Pokémon based on customer specifications.

Web-Based Dashboard – Order tracking and management UI.

Multi-Game Expansion – Support for other titles like Animal Crossing item trading.

Multi-Pi Scaling – Distributing order fulfillment across multiple Raspberry Pis. 

## Contributing

This project is constantly evolving! Contributions and suggestions are welcome. Feel free to submit a pull request or open an issue. The Shiny Vault isn’t just a bot—it’s a fully automated trading system, built to be efficient, scalable, and future-proof. 

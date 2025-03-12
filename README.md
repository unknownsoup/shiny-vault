# The Shiny Vault
This program processes and fufill orders for pokemon in Pokemon Scarlet and Violet via ebay api, SQL, a discord bot, and an emulated Nintendo Switch Pro Controller using NXBT via raspberry pi.

First, the buyer makes an order on eBay and the order information is put in SQL. Then, if the buyer decides they want to use the trade bot, they join the discord and use "!starttrade" in the bot chat. The bot then gets the buyers eBay username (for verification) and in turn the bot grabs the product ID from the database: searching with the buyer's eBay username. The bot then prompts the buyer to provide their IGN and trade-code. If everything is provided correctly, the trade will execute and the order will be fulfilled. If not, then the bot communicates with the user in discord accordingly. 


# Future Plans
- Create website to process orders with discord
    - Pokemon trading section for people to post Pokemon trades
- Expand bot trading to Animal Crossing

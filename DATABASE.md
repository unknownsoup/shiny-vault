# Shiny Vault Database Schema

## Customers Table
Stores customer details.

| Column          | Type      | Description                 |
|----------------|----------|-----------------------------|
| id             | INTEGER  | Primary Key                 |
| ebay_user      | TEXT     | eBay username (Unique)      |
| discord_user   | TEXT     | Discord ID (Optional)       |
| total_orders   | INTEGER  | Total number of orders      |
| created_at     | TIMESTAMP | Timestamp of account creation |


## Orders Table
Tracks Pokémon orders from eBay.

| Column     | Type      | Description                 |
|-----------|----------|-----------------------------|
| order_id  | INTEGER  | Primary Key                 |
| listing_id | TEXT    | Unique eBay Order Number    |
| ebay_username | TEXT | Stores eBay Username        |
| SKU       | TEXT     | location of the item in virtual db | 
| Price     | DECIMAL(10,2) | Price of item          |
| status    | ENUM     | pending, in_progress, completed, canceled |
| created_at | TIMESTAMP | Order creation timestamp  |


## Products Table
Tracks all products avaliable and where they're located in the virtual boxes database that the bot uses.

| Column     | Type      | Description                 |
|-----------|----------|-----------------------------|
| product_id | INTEGER | Primary Key                 |
| listing_id | TEXT    | Unique eBay Order Number    |
| storage_location | TEXT | Location inside database: "000-960" | 

## TradeQueue Table
Tracks ongoing orders from eBay.

| Column     | Type      | Description                 |
|-----------|----------|-----------------------------|
| queue_id  | INTEGER  | Primary Key                 |
| trade_code | INTEGER | 8 Digit Code to trade       | 
| storage_location | TEXT | SKU Pulled From Products at insert time | 
| status    | ENUM       | pending, in_progress, completed, canceled |
| created_at | TIMESTAMP | Order creation timestamp  |
| updated_at | TIMESTAMP | Last updated timestamp    |


# Shiny Vault Database Schema

## Customers Table
Stores customer details.

| Column          | Type      | Description                 |
|----------------|----------|-----------------------------|
| id             | INTEGER  | Primary Key                 |
| ebay_username  | TEXT     | eBay username (Unique)      |
| discord_id     | TEXT     | Discord ID (Optional)       |
| total_orders   | INTEGER  | Total number of orders      |
| created_at     | TIMESTAMP | Timestamp of account creation |


## Orders Table
Tracks Pokémon orders from eBay.

| Column     | Type      | Description                 |
|-----------|----------|-----------------------------|
| order_id  | INTEGER  | Primary Key                 |
| customer_id | INTEGER | Customer   |
| listing_id | TEXT    | Unique eBay Order Number    |
| ebay_username | TEXT | Stores eBay Username        |
| SKU       | TEXT     | location of the item in virtual db | 
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
| order_id  | INTEGER  | Foreign Key -> Orders       |
| listing_id | TEXT    | Links Orders to Products    | 
| trade_code | INTEGER | 8 Digit Code to trade       | 
| SKU       | TEXT     | Foreign Key -> Orders       | 
| storage_location | TEXT | Pulled From Products at insert time | 
| status    | ENUM       | pending, in_progress, completed, canceled |
| created_at | TIMESTAMP | Order creation timestamp  |
| updated_at | TIMESTAMP | Last updated timestamp    |


-- Create Database (if not already created)
CREATE DATABASE IF NOT EXISTS shiny_vault;
USE shiny_vault;

-- Customers Table
CREATE TABLE IF NOT EXISTS Customers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ebay_user VARCHAR(255) UNIQUE NOT NULL,
    discord_user VARCHAR(255) NULL DEFAULT NULL,
    total_orders INT DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (ebay_user) REFERENCES Orders(ebay_username)
);

-- Orders Table
CREATE TABLE IF NOT EXISTS Orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    listing_id VARCHAR(50) NOT NULL,
    ebay_username VARCHAR(255) NOT NULL,
    sku VARCHAR(50) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status ENUM('pending', 'in_progress', 'completed', 'canceled') DEFAULT 'pending'
);

-- TradeQueue Table
CREATE TABLE IF NOT EXISTS TradeQueue (
    queue_id INT AUTO_INCREMENT PRIMARY KEY,
    trade_code VARCHAR(20) NOT NULL,
    storage_location VARCHAR(50) NOT NULL,
    status ENUM('waiting', 'trading', 'completed', 'failed') DEFAULT 'waiting',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Products Table
CREATE TABLE IF NOT EXISTS Products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    listing_id VARCHAR(50) UNIQUE NOT NULL,
    storage_location VARCHAR(50) NOT NULL
);

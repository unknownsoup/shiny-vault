# SQL SET UP 
import mysql.connector
from ..ebay.ebay_api import EBay_Handler

mydb = mysql.connector.connect(
  host="localhost",
  user="braedon",
  password="root",
  database="shiny_vault"
)

mycursor = mydb.cursor()

mycursor.execute("DESCRIBE tradequeue")

for x in mycursor:
  print(x)

class sqlrequests():

    mydb = mysql.connector.connect(
      host="localhost",
      user="braedon",
      password="root",
      database="shiny_vault"
    )

    mycursor = mydb.cursor()

    # Create a new order in the database
    def create_new_order(): # listing_id, ebay_username, sku, price, created at, status
        
        results = EBay_Handler.fetch_orders_from_ebay()

        ebay_user = results[0]
        lineitemid = results[1]
        sku = results[2]
        price = results[3]
        status = "pending"

        sql = """INSERT INTO orders (listing_id, ebay_username, sku, price, status) 
                 VALUES (%s, %s, %s, %s, %s)"""
        values = (lineitemid, ebay_user, sku, price, status)

        mycursor.execute(sql, values)
        mydb.commit()  # Commit changes to the database
        return

    
    def verify_ebay_username(username):
    # Check if the username exists and has a pending order
      sql = """
          SELECT ebay_username FROM orders 
          WHERE ebay_username = %s AND status = 'pending'
          """
      
      mycursor.execute(sql, (username,))
      result = mycursor.fetchone()  # Fetch one result

      if result:  # If a pending order exists
          update_sql = """
                        UPDATE orders 
                        SET status = 'in_progress' 
                        WHERE ebay_username = %s
                        """
          mycursor.execute(update_sql, (username,))

          mydb.commit()  # Save changes to the database

          return True  # Order was updated successfully
      
      return False  # No pending order found


    def order_info_for_bot(username):
       r = ("", "", "")
       return r
    

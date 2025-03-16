# SQL SET UP 
import mysql.connector


mydb = mysql.connector.connect(
  host="localhost",
  user="braedon",
  password="root",
  database="shiny_vault"
)

mycursor = mydb.cursor()

mycursor.execute("DESCRIBE orders")

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

    # TODO FILL IN VALUES TO BE INSERTED, GRABBED FROM EBAY API 
    def create_new_order(): # listing_id, ebay_username, sku, price, created at, status
        mycursor.execute("INSERT INTO orders (listing_id), (ebay_username), (sku), (price), (status)" 
                         "VALUES ()")
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
    

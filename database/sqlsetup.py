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
        # check if the username exists AND that the 
        mycursor.execute(f"SELECT ebay_username"
                         "FROM orders"
                         "WHERE EXISTS"
                         "(SELECT ebay_username FROM orders WHERE ebay_username = {username} AND status = pending")

    def get_order_listingID():
        # look in order table
        return ""
    
    def get_order_ebay_username():
        # look in order table
        return ""
    
    def get_order_sku():
        # use the 
        return ""
    

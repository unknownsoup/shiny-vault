# fetch orders from ebay and parse the response
import json 

def fetch_orders_from_ebay():
    # This function would typically make an API call to eBay to fetch orders
    # For this example, we will load a sample JSON response from a file
    # sample ebay response for testing
    with open("C:\\Users\\braed\\shiny-vault\\ebay\\sample_json_reponse.json", "r", encoding="utf-8") as file:
        ebay_response = json.load(file)

    # Extract necessary details
    parsed_data = []
    for order in ebay_response.get("orders", []):
        buyer_username = order.get("buyer", {}).get("username", "N/A")
        
        for item in order.get("lineItems", []):
            line_item_id = item.get("lineItemId", "N/A")
            sku = item.get("sku", "N/A")
            line_item_cost = item.get("lineItemCost", {}).get("value", "N/A")
            
            parsed_data.append({
                buyer_username,
                line_item_id,
                sku,
                line_item_cost
            })

    # Display results
    print(f"Parsed Data: {parsed_data}")
    return parsed_data
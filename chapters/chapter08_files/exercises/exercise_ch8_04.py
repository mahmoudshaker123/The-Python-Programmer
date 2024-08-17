# Exercise 08_04 - Inventory Management System
# Write a CSV file containing inventory data and generates a report on stock levels and restock alerts.
# The CSV file contains columns: item_name, item_id, quantity, and price.
# Read the CSV file and calculate the total value of the inventory.
# Identify items with stock levels below the restock threshold and store them in a list.
# Return a dictionary containing the total inventory value and the list of items that need restocking.

# Example data.csv:
# item_name,item_id,quantity,price
# Apple,1,100,0.5
# Banana,2,200,0.3
# Orange,3,150,0.4

# The function should return:

# {
#     "total_inventory_value": 140.0,
#     "restock_alerts": [
#         {"item_name": "Apple", "item_id": 1, "quantity": 100, "price": 0.5},
#         {"item_name": "Orange", "item_id": 3, "quantity": 150, "price": 0.4},
#     ],
# }

# The restock threshold is 200 items.
# The total inventory value is calculated as the sum of quantity * price for each item.
# The restock alerts are items with a quantity below the restock threshold.


def inventory_management(
    file_name: str, restock_threshold: int
) -> dict[str, list[dict[str, str]]]:
    # Your code should go here.

    ...

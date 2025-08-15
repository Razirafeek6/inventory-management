import json

# -------------------------------
# Inventory Management System
# -------------------------------
# Features:
# 1. View Items
# 2. Add Items
# 3. Remove Items
# 4. Search Item
# 5. Update Item Quantity
# 6. Sort Items
# 7. Exit
# Data is saved in a JSON file for persistence.
# -------------------------------

# Step 1: Load stock from file (or create if not exists)
try:
    with open("stock.json", "r") as f:
        stock = json.load(f)
except FileNotFoundError:
    stock = {}

def save_stock():
    """Function to save stock to file"""
    with open("stock.json", "w") as f:
        json.dump(stock, f)

while True:
    choice = int(input("\n----- MENU -----\n"
                       "1. View Items\n"
                       "2. Add Items\n"
                       "3. Remove Items\n"
                       "4. Search Item\n"
                       "5. Update Item Quantity\n"
                       "6. Sort Items\n"
                       "7. Exit\n"
                       "Select: "))

    if choice == 1:
        print("\nAvailable Items:")
        for item, quantity in stock.items():
            print(f"{item} : {quantity}")

    elif choice == 2:
        user_item = input("Enter the item to add: ")
        user_quantity = int(input("Enter the quantity: "))
        stock[user_item] = stock.get(user_item, 0) + user_quantity
        save_stock()
        print("✅ Stock updated successfully!")

    elif choice == 3:
        user_sold_out = input("Enter the sold-out item: ")
        if user_sold_out in stock:
            stock.pop(user_sold_out)
            save_stock()
            print(f"❌ {user_sold_out} removed from stock.")
        else:
            print("⚠ Item not found.")

    elif choice == 4:
        search_item = input("Enter the item to search: ")
        if search_item in stock:
            print(f"✅ {search_item} is available. Quantity: {stock[search_item]}")
        else:
            print("❌ Searched item does not exist.")

    elif choice == 5:
        update_item = input("Enter the item to update the quantity: ")
        if update_item in stock:
            old_quantity = stock[update_item]
            update_quantity = int(input("Enter the new quantity: "))
            stock[update_item] = update_quantity
            save_stock()
            print(f"🔄 Quantity for {update_item} updated from {old_quantity} to {update_quantity}.")
        else:
            print("⚠ Item doesn't exist.")

    elif choice == 6:
        print("\n--- SORT MENU ---")
        print("1. Sort by Name (A-Z)")
        print("2. Sort by Quantity (High → Low)")
        sort_choice = int(input("Select: "))

        if sort_choice == 1:
            sorted_stock = dict(sorted(stock.items()))
            print("\n📋 Items sorted by name:")
            for item, quantity in sorted_stock.items():
                print(f"{item} : {quantity}")

        elif sort_choice == 2:
            sorted_stock = dict(sorted(stock.items(), key=lambda x: x[1], reverse=True))
            print("\n📋 Items sorted by quantity (high → low):")
            for item, quantity in sorted_stock.items():
                print(f"{item} : {quantity}")
        else:
            print("⚠ Invalid sort choice!")

    elif choice == 7:
        print("👋 Exiting. Thank you!")
        break

    else:
        print("⚠ Invalid choice!")

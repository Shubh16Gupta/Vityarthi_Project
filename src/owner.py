from inventory import loadInventory, saveInventory, logActivity
#from this owner catalog will be updated
def addItem():
    inv = loadInventory()
    name = input("New product name:").strip()
    try:
        price = float(input("Price: $"))
        qty = int(input("quantity:"))
        discount = float(input("Discount %:"))
    except:
        print("Enter valid numbers!")
        return
    location = input("location:").strip()

    inv[name] = {
        "sellingPrice": price,
        "stockQuantity": qty,
        "priceDiscountPercent": discount,
        "storageLocation": location
    }
    saveInventory(inv)
    logActivity(f"Added new product: {name}, qty: {qty}")
    print(f"{name} added to inventory.")
#to add the stock
def addStock():
    inv = loadInventory()
    name = input("Product to add stock:").strip()
    if name not in inv:
        print("Product not found!")
        return
    try:
        qty = int(input("How many units to add:"))
    except:
        print("Enter a number!")
        return
    inv[name]["stockQuantity"]+= qty
    saveInventory(inv)
    logActivity(f"Added {qty} units to {name}")
    print("Stock updated.")
#this will show the inventory
def showInventory():
    inv = loadInventory()
    if not inv:
        print("Inventory is empty.")
        return
    print("\n--Inventory--")
    for name, d in inv.items():
        print(f"{name}: ${d['sellingPrice']}, Qty: {d['stockQuantity']}, Discount: {d['priceDiscountPercent']}%, Loc: {d['storageLocation']}")
#to check the stock
def check_low_stock():
    inv = loadInventory()
    low = False
    print("\n--Low Stock--")
    for name, d in inv.items():
        if d['stockQuantity'] <= 5:
            print(f"{name}: only {d['stockQuantity']} left!")
            low = True
    if not low:
        print("All products have enough stock.")
#ui on the terminal
def ownerMenu():
    while True:
        print("\n==OWNER MENU==")
        print("1.Add new product")
        print("2.Replenish stock")
        print("3.Show inventory")
        print("4.Check low stock")
        print("5.Exit")
        choice = input("Option:").strip()
        if choice == "1":
            addItem()
        elif choice == "2":
            addStock()
        elif choice == "3":
            showInventory()
        elif choice == "4":
            check_low_stock()
        elif choice == "5":
            break
        else:
            print("Invalid choice!")
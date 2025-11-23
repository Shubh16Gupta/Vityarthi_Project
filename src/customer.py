from inventory import loadInventory, saveInventory, saveCustomerBill
def Transaction():
    invt = loadInventory()
    cart = []
    total = 0

    print("\n--New Customer--")
    while True:
        item = input("Enter product name (or 'done'): ").strip()
        if item.lower() == "done":
            break
        if item not in invt:
            print("Product not found!")
            continue
        try:
            qty = int(input(f"Quantity for {item}: "))
        except:
            print("Enter a valid number!")
            continue
        if qty > invt[item]["stockQuantity"]:
            print(f"Only {invt[item]['stockQuantity']} left!")
            continue
        price = invt[item]["sellingPrice"]
        discount = invt[item]["priceDiscountPercent"]
        line_total = qty * price * (1 - discount / 100)
        cart.append((item, qty, price, discount, line_total))
        total += line_total
        invt[item]["stockQuantity"] -= qty

    if not cart:
        print("No items purchased. Transaction cancelled.")
        return
    saveInventory(invt)
    print("\n--BILL--")
    for name, qty, price, disc, amt in cart:
        print(f"{name} x{qty} = ${amt:.2f} ({disc}% off)")
    print(f"TOTAL: ${total:.2f}")
    pay_method = input("Payment method: ").strip()
    cust_name = input("Customer name: ").strip() or "Guest"
    saveCustomerBill(cust_name, cart, total, pay_method)
    print("Bill saved successfully")
#to check the price
def checkPrice():
    invt = loadInventory()
    item = input("Product name to check: ").strip()
    if item in invt:
        d = invt[item]
        print(f"{item}: ${d['sellingPrice']}, Discount: {d['priceDiscountPercent']}%")
    else:
        print("not found!")
#to locate the price
def locateProduct():
    invt = loadInventory()
    item = input("Product name to locate: ").strip()
    if item in invt:
        print(f"{item} is located at: {invt[item]['storageLocation']}")
    else:
        print("not found!")
#to display the coustomer menu
def customerMenu():
    while True:
        print("\n==CUSTOMER MENU==")
        print("1.Buy products / generate bill")
        print("2.Check product price")
        print("3.Locate product")
        print("4.Exit")
        choice = input("Option:").strip()
        if choice == "1":
            Transaction()
        elif choice == "2":
            checkPrice()
        elif choice == "3":
            locateProduct()
        elif choice == "4":
            break
        else:
            print("Invalid choice!")
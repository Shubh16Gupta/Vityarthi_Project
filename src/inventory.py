import os
from datetime import datetime
PRODUCT = ""
CUSTOMER = ""
OWNER = ""
def location(productFile, customerFile, ownerFile):
    global PRODUCT, CUSTOMER, OWNER
    PRODUCT = productFile
    CUSTOMER = customerFile
    OWNER = ownerFile
#to load the inventory
def loadInventory():
    inventory = {}
    if os.path.exists(PRODUCT):
        with open(PRODUCT, "r") as f:
            for line in f:
                if line.strip():
                    name, price, qty, discount, location = line.strip().split("|")
                    inventory[name] = {
                        "sellingPrice": float(price),
                        "stockQuantity": int(qty),
                        "priceDiscountPercent": float(discount),
                        "storageLocation": location
                    }
    return inventory
#to save the inventory
def saveInventory(invt):
    try:
        with open(PRODUCT, "w") as f:
            for name, details in invt.items():
                f.write(f"{name}|{details['sellingPrice']}|{details['stockQuantity']}|{details['priceDiscountPercent']}|{details['storageLocation']}\n")
    except:
        print("Error saving products file!")
#login activity
def logActivity(msg):
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        with open(OWNER, "a") as f:
            f.write(f"[{ts}] {msg}\n")
    except:
        print("Error writing owner log!")
#to save the bill 
def saveCustomerBill(cust_name, cart, total, pay_method):
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        with open(CUSTOMER, "a") as f:
            f.write(f"[{ts}] Customer: {cust_name} | Total: ${total:.2f} | Payment: {pay_method}\n")
            for item, qty, price, disc, amt in cart:
                f.write(f"  {item} x{qty} = ${amt:.2f} ({disc}% off)\n")
            f.write("\n")
    except:
        print("Error saving customer bill!")
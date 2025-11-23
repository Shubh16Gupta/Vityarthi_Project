import os
from inventory import location
from owner import ownerMenu
from customer import customerMenu
BASIC_DATA = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(BASIC_DATA, "data")
if not os.path.exists(DATA):
    os.makedirs(DATA)
PRODUCT = os.path.join(DATA, "products.txt")
CUSTOMER = os.path.join(DATA, "customers.txt")
OWNER = os.path.join(DATA, "owner.txt")
for f in [PRODUCT, CUSTOMER, OWNER]:
    if not os.path.exists(f):
        open(f, "a").close()
location(PRODUCT, CUSTOMER, OWNER)
#this will be showed to the user in the terminal  
def main():
    while True:
        print("\n==MALL BILLING SYSTEM==")
        print("1.Owner")
        print("2.Customer")
        print("3.Exit")
        choice=input("Enter choice:").strip()
        if choice=="1":
            ownerMenu()
        elif choice=="2":
            customerMenu()
        elif choice=="3":
            print("Exit successfully")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
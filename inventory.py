# inventory.py

# Import tabulate
from tabulate import tabulate


class Shoes:
    def __init__(self, country, code, product, cost, quantity):  # Constructor
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):  # get_cost value
        return self.cost

    def get_quantity(self):  # get_quantity value
        return self.quantity

    def __str__(self):  # Return a string representation of the class Shoes
        return f"Country: {self.country}, Code: {self.code}, Product: {self.product}, Cost: {self.cost}, Quantity: {self.quantity}"


# Empty list to store shoe objects
shoes_list = []


def read_shoes_data():
    try:
        with open("inventory.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                if line.strip() == 'Country,Code,Product,Cost,Quantity':
                    continue  # Skip the first line with column headers
                data = line.strip().split(",")
                country = data[0]
                code = data[1]
                product = data[2]
                cost = float(data[3])
                quantity = int(data[4])
                shoe = Shoes(country, code, product, cost, quantity)
                shoes_list.append(shoe)
        print("Data from inventory.txt has been successfully loaded.")
    except FileNotFoundError:
        print("Error: inventory.txt file not found.")
    except Exception as e:
        print("Error: ", e)


def capture_shoes():  # Allow user to capture data about a shoe,
    # create object and append inside shoe list
    country = input("Enter country: ")
    code = input("Enter code: ")
    product = input("Enter product: ")
    cost = float(input("Enter cost: "))
    quantity = int(input("Enter quantity: "))
    shoe = Shoes(country, code, product, cost, quantity)
    shoes_list.append(shoe)


def view_all():  # view all shoes list
    if len(shoes_list) > 0:
        headers = ["Country", "Code", "Product", "Cost", "Quantity"]
        data = [[shoe.country, shoe.code, shoe.product, shoe.cost, shoe.quantity] for shoe in shoes_list]
        print(tabulate(data, headers=headers))
    else:
        print("No shoes in inventory.")


def update_inventory_file():  # update on the file "inventory.txt" shoe
    try:
        with open("inventory.txt", "w") as file:  # Open inventory.txt in write mode
            for shoe in shoes_list:
                line = f"{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}\n"
                file.write(line)
        print("Inventory file updated successfully.")
    except FileNotFoundError:
        print("Error: File not found.")


def re_stock():  # Find the shoe object, then ask if user wants to add
    # quantity of those shoes and update on the file "inventory.txt" this shoe
    if len(shoes_list) > 0:
        lowest_quantity = float('inf')
        shoe_to_restock = None
        for shoe in shoes_list:
            if shoe.quantity < lowest_quantity:
                lowest_quantity = shoe.quantity
                shoe_to_restock = shoe

        if shoe_to_restock:
            print("Shoe to restock:")
            print(shoe_to_restock)

            choice = input("Do you want to add quantity to this shoe? (y/n): ")
            if choice.lower() == 'y':
                quantity_to_add = int(input("Enter quantity to add: "))
                shoe_to_restock.quantity += quantity_to_add
                print("Quantity updated successfully.")
                update_inventory_file()
        else:
            print("No shoes need restocking.")
    else:
        print("No shoes in inventory.")


def search_shoe():  # search shoe  given the shoe code
    if len(shoes_list) > 0:
        code = input("Enter shoe code to search: ")
        for shoe in shoes_list:
            if shoe.code == code:
                print("Shoe found:")
                print(shoe)
                break
        else:
            print("Shoe not found.")
    else:
        print("No shoes in inventory.")


def value_per_item():  # Total value per item: $
    if len(shoes_list) > 0:
        total_value = 0
        for shoe in shoes_list:
            total_value += shoe.cost * shoe.quantity
        print("Total value per item: $", total_value)
    else:
        print("No shoes in inventory.")


def highest_qty():  # Product with highest quantity:
    max_quantity = 0
    max_quantity_shoe = None
    for shoe in shoes_list:
        if shoe.quantity > max_quantity:
            max_quantity = shoe.quantity
            max_quantity_shoe = shoe

    if max_quantity_shoe:
        print("Product with highest quantity:")
        print(max_quantity_shoe)
    else:
        print("No shoes in inventory")


# Main menu
while True:
    print("1. Read shoes data from file")
    print("2. Capture shoe data")
    print("3. View all shoes")
    print("4. Re-stock shoes")
    print("5. search shoe by code")
    print("6. Total value per item: $")
    print("7. Product with highest quantity")
    print("8. Exit")
    choice = input("Enter your choice (1/2/3/4/5/6/7/8): ")
    if choice == '1':
        read_shoes_data()
    elif choice == '2':
        capture_shoes()
    elif choice == '3':
        view_all()
    elif choice == '4':
        re_stock()
    elif choice == '5':
        search_shoe()
    elif choice == '6':
        value_per_item()
    elif choice == '7':
        highest_qty()
    elif choice == '8':
        print("Come back anytime...")
        break
    else:
        print("Invalid choice. Please try again.")
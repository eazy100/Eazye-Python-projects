
class Shoe:
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        return self.cost

    def get_quantity(self):
        return self.quantity

    def __str__(self):
        return f"Country:{self.country},Code:{self.code},Product:{self.product},Cost:{self.cost},Quantity:{self.quantity}"


shoe_list = []


def read_shoes_data():
    try:
        with open("inventory.txt", "r") as file:
            next(file)  # Skip the first line
            for line in file:
                data = line.strip().split(",")
                country, code, product, cost, quantity = data
                shoe = Shoe(country, code, product, float(cost), int(quantity))
                shoe_list.append(shoe)
        print("Shoes loaded successfully!")
    except FileNotFoundError:
        print("File not found.")


def capture_shoes():
    try:
        country = input("Enter country: ")
        code = input("Enter code: ")
        product = input("Enter product: ")
        cost = float(input("Enter cost: "))
        quantity = int(input("Enter quantity: "))
        shoe = Shoe(country, code, product, cost, quantity)
        shoe_list.append(shoe)
        print("Shoe added successfully!")
    except ValueError:
        print("Invalid input! Please enter valid data.")


def view_all():
    for shoe in shoe_list:
        print(shoe)


def re_stock():
    min_quantity_shoe = min(shoe_list, key=lambda x: x.quantity)
    print(f"The shoe to restock is: {min_quantity_shoe}")
    try:
        restock_quantity = int(input("Enter quantity to restock: "))
        min_quantity_shoe.quantity += restock_quantity
        print(f"Quantity of {min_quantity_shoe.product} updated to {min_quantity_shoe.quantity}")
    except ValueError:
        print("Invalid input! Please enter a valid quantity.")


def search_shoe():
    code = input("Enter the code of the shoe to search: ")
    for shoe in shoe_list:
        if shoe.code == code:
            print(shoe)
            return
    print("Shoe not found!")


def value_per_item():
    for shoe in shoe_list:
        value = shoe.cost * shoe.quantity
        print(f"Product: {shoe.product}, Total Value: {value}")


def highest_qty():
    max_quantity_shoe = max(shoe_list, key=lambda x: x.quantity)
    print(f"The shoe with the highest quantity is: {max_quantity_shoe.product}, Quantity: {max_quantity_shoe.quantity}")


def main_menu():
    while True:
        print("\n=====MAIN MENU=====")
        print("1. Read shoes data from file")
        print("2. Capture new shoe")
        print("3. View all shoes")
        print("4. Restock shoe")
        print("5. Search shoe")
        print("6. Value per item")
        print("7. Highest quantity shoe")
        print("8. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            read_shoes_data()
        elif choice == "2":
            capture_shoes()
        elif choice == "3":
            view_all()
        elif choice == "4":
            re_stock()
        elif choice == "5":
            search_shoe()
        elif choice == "6":
            value_per_item()
        elif choice == "7":
            highest_qty()
        elif choice == "8":
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 8.")


if __name__ == "__main__":
    main_menu()
 
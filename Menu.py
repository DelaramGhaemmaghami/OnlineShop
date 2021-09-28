class Menu:
    @staticmethod
    def main_menu():
        options = ["1- Register", "2- log in", "3- Exit\n"]

        print("\n" + "\u2500" * 40 + " << MENU >> " + "\u2500" * 40 + "\n")

        for option in options:
            print(option)

        while True:
            user_option = input("Please enter the number of your CHOICE: ")

            if user_option in ["1", "2", "3"] or user_option == "":
                return user_option

            else:
                print("\nINVALID INPUT! Please choose a number between 1 to 3 or press ENTER to exit.")
                continue

    @staticmethod
    def role_menu():
        roles = ["1- Manager", "2- Customer\n"]

        print("\n" + "\u2500" * 40 + " << ROLE >> " + "\u2500" * 40 + "\n")

        for role in roles:
            if roles.index(role) == -1:
                print("\n")
            print(role)

        while True:
            user_role = input("Please enter the number of your ROLE: ")

            if user_role in ["1", "2"]:
                return user_role

            else:
                print("\nINVALID INPUT! Please choose a number between 1 and 2.")
                continue

    @staticmethod
    def manager_menu():
        options = ["1- Record the list of goods and specifications of each",
                   "2- View inventory", "3- View customer purchase invoices", "4- Invoice Search",
                   "5- View the profile list of all customers", "6- Customer block", "7- Logout\n"]

        print("\n" + "\u2500" * 40 + " << MENU >> " + "\u2500" * 40 + "\n")

        print("Role: Store Manager\n")

        for option in options:
            if options.index(option) == -1:
                print("\n")
            print(option)

        while True:
            user_option = input("Please enter the number of your CHOICE: ")

            if user_option.isnumeric() and int(user_option) in range(1, 8):
                return user_option

            else:
                print("\nINVALID INPUT! Please choose a number between 1 to 7 or press ENTER to exit.")
                continue

    @staticmethod
    def customer_menu():
        options = ["1- Sign in", "2- View previous invoices", "3- View list of stores", "4- Store Search",
                   "5- Select a store", "6- View the list of goods", "7- Product search", "8- Select items",
                   "9- Show pre-invoice", "10- Confirm purchase or edit it", "11- Logout\n"]

        print("\n" + "\u2500" * 40 + " << MENU >> " + "\u2500" * 40 + "\n")

        print("Role: Customer\n")

        for option in options:
            if options.index(option) == -1:
                print("\n")
            print(option)

        while True:
            user_option = input("Please enter the number of your CHOICE: ")

            if user_option.isnumeric() and int(user_option) in range(1, 12):
                return user_option

            else:
                print("\nINVALID INPUT! Please choose a number between 1 to 10 or press ENTER to exit.")
                continue

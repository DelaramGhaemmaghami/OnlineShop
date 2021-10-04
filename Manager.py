import re
import csv
import logging
import random
import datetime
import FileHandler
import Manager_functions

from prettytable import PrettyTable

phone_regex = "(\+98|0)?9\d{9}"

pass_word_regex = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"


class Manager:
    def __init__(self, user_name, pass_word, store_name, start_time, close_time):
        self.user_name = user_name
        self.pass_word = Manager_functions.password_hashing(pass_word)
        self.store_name = store_name
        self.start_time = start_time
        self.close_time = close_time

        manager_dict = self.__dict__

        managers_file = FileHandler.FileHandler("Manager.csv")
        managers_file.add_to_file(manager_dict)

        existed_store_dict = {"store_name": self.store_name}

        existed_store_file = FileHandler.FileHandler("existed_store.csv")
        existed_store_file.add_to_file(existed_store_dict)

    @classmethod
    def register(cls):

        print("\n" + "\u2500" * 45 + " << REGISTER >> " + "\u2500" * 45 + "\n")

        file = FileHandler.FileHandler("Manager.csv")

        while True:
            user_name = input("Please enter your PHONE NUMBER: ")

            does_exist = False

            if re.search(phone_regex, user_name):

                if not file.is_exist():
                    pass

                else:
                    good_reader = csv.reader(open("Manager.csv"))
                    lines = list(good_reader)

                    for i in range(len(lines)):
                        if lines[i][0] == user_name:
                            print("\nWARNING! This user name exists.")

                            logging.basicConfig(level=logging.WARNING, filename="warnings.log", filemode="a",
                                                format='%(name)s - %(levelname)s - %(message)s')
                            logging.warning(f"""{user_name} entered an existed name /"""
                                            f"""date_time -> {datetime.datetime.now()}""")

                            does_exist = True

            else:
                print("\nERROR! Please enter a VALID PHONE NUMBER.")

                logging.basicConfig(level=logging.ERROR, filename="errors.log", filemode="a",
                                    format='%(name)s - %(levelname)s - %(message)s')
                logging.error(f"""{user_name} entered an invalid phone number /"""
                              f"""date_time -> {datetime.datetime.now()}""")

                continue

            if does_exist:
                continue
            break

        while True:
            pass_word = input("Please enter your PASS WORD: ")

            pat = re.compile(pass_word_regex)
            mat = re.search(pat, pass_word)

            if mat:
                break

            else:
                print("""\nERROR! Please enter a valid PASS WORD, which contains capital letters,"""
                      """small letters, number and symbols.""")

                logging.basicConfig(level=logging.ERROR, filename="errors.log", filemode="a",
                                    format='%(name)s - %(levelname)s - %(message)s')
                logging.error(f"""{user_name} entered an invalid pass word /"""
                              f"""date_time -> {datetime.datetime.now()}""")

                continue

        while True:
            confirm_password = input("Please enter your PASS WORD again: ")

            if pass_word == confirm_password:
                break

            else:
                print("""\nWARNING! The second pass word that you entered does not match the first one, """
                      """please enter it again.""")

        while True:
            store_name = input("Please enter the name of the store: ")

            if store_name.isalnum():
                break

            else:
                print("\nERROR! Please enter a name which contains only alphabets and numbers.")

                logging.basicConfig(level=logging.ERROR, filename="errors.log", filemode="a",
                                    format='%(name)s - %(levelname)s - %(message)s')
                logging.error(f"""Pass word confirmation failed for {user_name} /"""
                              f"""date_time -> {datetime.datetime.now()}""")

                continue

        while True:
            start_time = Manager_functions.get_and_check_open()
            close_time = Manager_functions.get_and_check_close()

            if close_time > start_time:
                print("\nRegistration completed successfully!\n")

                logging.basicConfig(level=logging.INFO, filename="register_manager.log", filemode="a",
                                    format='%(name)s - %(levelname)s - %(message)s')
                logging.info(f"{user_name} registered / date_time -> {datetime.datetime.now()}")

                return cls(user_name, pass_word, store_name, start_time, close_time)

            else:
                print("\nERROR! End time should be greater than start time.")

                logging.basicConfig(level=logging.ERROR, filename="errors.log", filemode="a",
                                    format='%(name)s - %(levelname)s - %(message)s')
                logging.error(f"""Open and close time are not compatible /"""
                              f"""date_time -> {datetime.datetime.now()}""")

                continue

    @staticmethod
    def sign_in():
        print("\n" + "\u2500" * 45 + " << SIGN IN >> " + "\u2500" * 45 + "\n")

        user_name = input("Please enter your USER NAME: ")
        pass_word = input("Please enter your PASS WORD: ")

        flag = False

        with open("Manager.csv") as file_reader:
            reader = csv.reader(file_reader)
            check = list(reader)

            for i in range(len(check)):
                if user_name == check[i][0] and Manager_functions.password_hashing(pass_word) == check[i][1]:
                    print(f"\n{user_name} has successfully signed in.")

                    logging.basicConfig(level=logging.INFO, filename="sign_in_manager.log", filemode="a",
                                        format='%(name)s - %(levelname)s - %(message)s')
                    logging.info(f"{user_name} signed in / date_time -> {datetime.datetime.now()}")

                    return user_name

        if not flag:
            print("\nWARNING! User name or password is wrong!")

            logging.basicConfig(level=logging.WARNING, filename="warnings.log", filemode="a",
                                format='%(name)s - %(levelname)s - %(message)s')
            logging.warning(f"{user_name} failed to log in / date_time -> {datetime.datetime.now()}")

            return False

    @staticmethod
    def warning(user_name):
        store_name = Manager_functions.find_store_name(user_name)

        file = FileHandler.FileHandler(f"{store_name}_invoice.csv")

        if file.is_exist():
            good_reader = csv.reader(open(f"{store_name}.csv"))

            good_filtered = list(filter(lambda p: "0" == p[4], good_reader))

            my_table = PrettyTable()
            my_table.field_names = ["barcode", "price", "brand", "name", "number_of_inventory", "exp_date"]

            if len(good_filtered) == 0:
                return True

            else:
                for item in good_filtered:
                    my_table.add_row(item)

                print("\n" + "\u2500" * 45 + "THESE GOODS ARE FINISHED!" + "\u2500" * 45 + "\n")
                print(my_table)

                logging.basicConfig(level=logging.INFO, filename=f"{store_name}_non_existent_goods.log", filemode="a",
                                    format='%(name)s - %(levelname)s - %(message)s')
                logging.info(f"{store_name} ran out of a product / date_time -> {datetime.datetime.now()}")

        else:
            return

    @staticmethod
    def record_goods(user_name):
        print("\n" + "\u2500" * 45 + " << RECORD GOODS >> " + "\u2500" * 45 + "\n")

        barcode = random.choice(range(10000000, 100000000))

        while True:
            price = input("Please enter the price: ")

            if price.isnumeric():
                break

            else:
                print("\nERROR! Please enter a number.")

                logging.basicConfig(level=logging.ERROR, filename="errors.log", filemode="a",
                                    format='%(name)s - %(levelname)s - %(message)s')
                logging.error(f"""{user_name} entered sth else instead of number /"""
                              f"""date_time -> {datetime.datetime.now()}""")

        while True:
            brand = input("Please enter the name of the brand: ")

            if brand.isalnum():
                break

            else:
                print("\nINVALID INPUT! Please enter a name which contains alphabets or numbers.")
                continue

        while True:
            name = input("Please enter the name of the good: ")

            if name.isalnum():
                break

            else:
                print("\nINVALID INPUT! Please enter a name which contains alphabets or numbers.")
                continue

        while True:
            number_of_inventory = input("Please enter the number of inventory: ")

            if number_of_inventory.isnumeric():
                break

            else:
                print("\nERROR! Please enter a number.")

                logging.basicConfig(level=logging.ERROR, filename="errors.log", filemode="a",
                                    format='%(name)s - %(levelname)s - %(message)s')
                logging.error(f"""{user_name} entered sth else instead of number /"""
                              f"""date_time -> {datetime.datetime.now()}""")

                continue

        while True:
            exp_date = input("Please enter the expiry date: ")

            if exp_date.isnumeric():
                break

            else:
                print("\nERROR! Please enter a number.")

                logging.basicConfig(level=logging.ERROR, filename="errors.log", filemode="a",
                                    format='%(name)s - %(levelname)s - %(message)s')
                logging.error(f"""{user_name} entered sth else instead of number /"""
                              f"""date_time -> {datetime.datetime.now()}""")

                continue

        good_dict = {"barcode": barcode, "price": price, "brand": brand, "name": name,
                     "number_of_inventory": number_of_inventory, "exp_date": exp_date}

        store_name = Manager_functions.find_store_name(user_name)

        store_file = FileHandler.FileHandler(f"{store_name}.csv")
        store_file.add_to_file(good_dict)

        print("\nThe product was successfully added!")

        logging.basicConfig(level=logging.INFO, filename="recorded_goods_manager.log", filemode="a",
                            format='%(name)s - %(levelname)s - %(message)s')
        logging.info(f"{user_name} recorded a good / date_time -> {datetime.datetime.now()}")

    @staticmethod
    def view(user_name):
        print("\n" + "\u2500" * 45 + " << INVENTORY LIST >> " + "\u2500" * 45 + "\n")

        inventory_table = PrettyTable()

        store_name = Manager_functions.find_store_name(user_name)

        inventory_table.field_names = ["barcode", "price", "brand", "name", "number_of_inventory", "exp_date"]

        with open(f"{store_name}.csv") as file_reader:
            csv_reader = list(csv.reader(file_reader))

            for row in csv_reader:
                if csv_reader.index(row) == 0:
                    continue
                inventory_table.add_row(row)

        return inventory_table

    @staticmethod
    def view_all_invoices(user_name):
        print("\n" + "\u2500" * 45 + " << INVOICES LIST >> " + "\u2500" * 45 + "\n")

        store_name = Manager_functions.find_store_name(user_name)

        invoice_reader = list(csv.reader(open(f"{store_name}_invoice.csv")))

        my_table = PrettyTable()
        my_table.field_names = ["date", "user_name", "brand", "good_name", "number", "total_amount"]

        for i in invoice_reader:
            if invoice_reader.index(i) == 0:
                continue
            my_table.add_row(i)

        print(my_table)

    @staticmethod
    def filter_invoices(user_name):
        print("\n" + "\u2500" * 45 + " << FILTERED INVOICES LIST >> " + "\u2500" * 45 + "\n")

        store_name = Manager_functions.find_store_name(user_name)

        invoice_reader = list(csv.reader(open(f"{store_name}_invoice.csv")))

        while True:
            search_basis = input("On what basis do you want to search?(user_name: u, date: d): ").lower()

            if search_basis.isalpha() and search_basis in ["u", "d"]:
                if search_basis.lower() == "u":

                    while True:
                        flag = False

                        customer_user_name = input("Please enter the USER NAME: ")

                        for i in range(len(invoice_reader)):
                            if str(list(invoice_reader)[i][1]) == customer_user_name:
                                inventory_filtered = list(filter(lambda p: customer_user_name == str(p[1]),
                                                                 invoice_reader))

                                my_table = PrettyTable()
                                my_table.field_names = ["date", "user_name", "brand", "good_name", "number",
                                                        "total_amount"]

                                for j in inventory_filtered:
                                    my_table.add_row(j)

                                print(my_table)
                                flag = True
                                break

                        if not flag:
                            print("\nWARNING! This user name does not exist.")
                            continue
                        else:
                            break

                if search_basis.lower() == "d":

                    while True:
                        flag = False

                        date = input("Please enter the DATE (EXAMPLE: 990203): ")

                        for i in range(len(list(invoice_reader))):
                            if str(list(invoice_reader)[i][0]) == date:
                                inventory_filtered = list(filter(lambda p: date == str(p[0]), invoice_reader))

                                my_table = PrettyTable()
                                my_table.field_names = ["date", "user_name", "brand", "good_name", "number",
                                                        "total_amount"]

                                for j in inventory_filtered:
                                    my_table.add_row(j)

                                print(my_table)
                                flag = True
                                break

                        if not flag:
                            print("\nWARNING! No transactions were made on this date.")
                            continue
                        else:
                            break

                break

            else:
                print("\nERROR! Please choose between 'u' or 'd'.")

                logging.basicConfig(level=logging.ERROR, filename="errors.log", filemode="a",
                                    format='%(name)s - %(levelname)s - %(message)s')
                logging.error(f"Invalid input / date_time -> {datetime.datetime.now()}")

                continue

    @staticmethod
    def customer_blocker(user_name):
        print("\n" + "\u2500" * 45 + " << CUSTOMER BLOCKER >> " + "\u2500" * 45 + "\n")

        customer_reader = csv.reader(open("Customer.csv"))
        lines = list(customer_reader)

        store_name = Manager_functions.find_store_name(user_name)

        while True:

            flag = False

            desired_number = input("Please enter the number that you want to block: ")

            for i in range(len(lines)):
                if lines[i][0] == desired_number:
                    block_dictionary = {"store": store_name, "blocked_user": desired_number}

                    file = FileHandler.FileHandler(f"{store_name}_blocked_users.csv")
                    file.add_to_file(block_dictionary)

                    print(f"{desired_number} has been successfully blocked.")
                    return

            if not flag:
                print(f"\nWARNING! {desired_number} does not exist.")
                continue

    @staticmethod
    def manager_invoices(date, store_name, user_name, brand, good_name, number, total_amount):

        invoice_dict = {"date": date, "user_name": user_name, "brand": brand, "good_name": good_name,
                        "number": number, "total_amount": total_amount}

        customer_invoice_file = FileHandler.FileHandler(f"{store_name}_invoice.csv")
        customer_invoice_file.add_to_file(invoice_dict)

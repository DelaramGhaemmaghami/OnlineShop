import re
import csv
import logging
import datetime
import FileHandler
import Manager
import Customer_functions

from prettytable import PrettyTable

phone_regex = "(\+98|0)?9\d{9}"

pass_word_regex = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"


class Customer:
    def __init__(self, user_name, pass_word):
        self.user_name = user_name
        self.pass_word = Customer_functions.password_hashing(pass_word)

        customer_dict = self.__dict__

        file = FileHandler.FileHandler("Customer.csv")
        file.add_to_file(customer_dict)

    @classmethod
    def register(cls):

        print("\n" + "\u2500" * 45 + " << REGISTER >> " + "\u2500" * 45 + "\n")

        file = FileHandler.FileHandler("Customer.csv")

        while True:
            user_name = input("Please enter your PHONE NUMBER: ")

            does_exist = False

            if re.search(phone_regex, user_name):

                if not file.is_exist():
                    pass

                else:
                    good_reader = csv.reader(open("Customer.csv"))
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
                print("""\nWARNING! Please enter a VALID PASS WORD, which contains capital letters,"""
                      """small letters, number and symbols.""")

                logging.basicConfig(level=logging.WARNING, filename="warnings.log", filemode="a",
                                    format='%(name)s - %(levelname)s - %(message)s')
                logging.warning(f"""{user_name} entered an invalid pass word /"""
                                f"""date_time -> {datetime.datetime.now()}""")

                continue

        while True:
            confirm_password = input("Please enter your PASS WORD again: ")

            if pass_word == confirm_password:
                break

            else:
                print("""\nERROR! The second pass word that you entered does not match the first one, """
                      """please enter it again.""")

                logging.basicConfig(level=logging.CRITICAL, filename="errors.log", filemode="a",
                                    format='%(name)s - %(levelname)s - %(message)s')
                logging.critical(f"""Pass word confirmation failed for {user_name} /"""
                                 f"""date_time -> {datetime.datetime.now()}""")

        print("\nRegistration completed successfully!")

        logging.basicConfig(level=logging.INFO, filename="register_customer.log", filemode="a",
                            format='%(name)s - %(levelname)s - %(message)s')
        logging.info(f"{user_name} registered / date_time -> {datetime.datetime.now()}")

        return cls(user_name, pass_word)

    @staticmethod
    def sign_in():
        print("\n" + "\u2500" * 45 + " << SIGN IN >> " + "\u2500" * 45 + "\n")

        user_name = input("Please enter your USER NAME: ")
        pass_word = input("Please enter your PASS WORD: ")

        flag = False

        with open("Customer.csv") as file_reader:
            reader = csv.reader(file_reader)
            check = list(reader)

            for i in range(len(check)):
                if user_name == check[i][0] and Customer_functions.password_hashing(pass_word) == check[i][1]:
                    print(f"\n{user_name} has successfully signed in.")

                    logging.basicConfig(level=logging.INFO, filename="sign_in_customer.log", filemode="a",
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
    def view_customers():
        print("\n" + "\u2500" * 35 + " << CUSTOMER LIST >> " + "\u2500" * 35 + "\n")

        customer_table = PrettyTable()
        customer_table.field_names = ["user_name", "pass_word"]

        with open("Customer.csv") as file_reader:
            csv_reader = list(csv.reader(file_reader))

            for row in csv_reader:
                if csv_reader.index(row) == 0:
                    continue
                customer_table.add_row(row)

        print(customer_table)

    @staticmethod
    def view_existed_stores():
        print("\n" + "\u2500" * 45 + " << EXISTED STORES >> " + "\u2500" * 45 + "\n")

        stores_table = PrettyTable()

        stores_table.field_names = ["store_names"]

        with open("existed_store.csv") as file_reader:
            csv_reader = list(csv.reader(file_reader))

            for row in csv_reader:
                if csv_reader.index(row) == 0:
                    continue

                stores_table.add_row(row)

        print(stores_table)

    @staticmethod
    def search_store():
        print("\n" + "\u2500" * 45 + " << SEARCH STORE >> " + "\u2500" * 45 + "\n")

        store_reader = list(csv.reader(open("existed_store.csv")))

        while True:
            flag = False

            name_search_store = input("Please enter your desired name of store: ")

            for i in range(len(store_reader)):

                if str(list(store_reader)[i][0]) == name_search_store:
                    print("The store name that you entered, exists.")
                    return name_search_store

            if not flag:
                print("ATTENTION! This name does not exist!")
                return False

    @staticmethod
    def inventory_update_customer(store_name, user_name, brand=None, required_name=None):
        print("\n" + "\u2500" * 45 + " << INVENTORY UPDATER >> " + "\u2500" * 45 + "\n")

        existence = False

        file_reader = list(csv.reader(open(f"{store_name}.csv")))

        if brand is None:
            brand = input("Enter your desired brand: ")

        if required_name is None:
            required_name = input("Enter the name you need: ")

        for i in range(len(file_reader)):
            if file_reader[i][3] == required_name:

                required_amount = Customer_functions.get_check_number()

                if int(required_amount) <= int(file_reader[i][4]):

                    store_reader = list(csv.reader(open(f"{store_name}.csv")))

                    for j in range(len(store_reader)):
                        if str(list(store_reader)[j][2]) == brand and str(list(store_reader)[i][3]) == required_name:
                            total_price = int(list(store_reader)[i][1]) * required_amount

                            if Customer.confirm_show_pre_invoice(datetime.date.today().strftime("%Y%m%d"), store_name,
                                                                 brand, required_name, required_amount, total_price):
                                Customer.customer_invoices(datetime.date.today().strftime("%Y%m%d"), user_name,
                                                           store_name, brand, required_name, required_amount,
                                                           total_price)

                                file_reader[i][4] = int(file_reader[i][4])
                                file_reader[i][4] -= int(required_amount)

                                print("\nINVENTORY UPDATED!")

                                with open(f"{store_name}.csv", "w", newline="") as file_writer:
                                    csv_writer = csv.writer(file_writer)
                                    csv_writer.writerows(file_reader)

                            else:
                                print("""Unfortunately you did not confirm your purchase invoice! """
                                      """I hope you will buy from our store next time.""")

                            return True

                else:
                    print("\nWARNING! The number you want is more than the stock.")
                    return False

        if not existence:
            print("\nWarning! This brand or product does not exist.")
            return False

    @staticmethod
    def view_goods(store_name):
        print("\n" + "\u2500" * 45 + " << INVENTORY LIST >> " + "\u2500" * 45 + "\n")

        inventory_table = PrettyTable()

        inventory_table.field_names = ["barcode", "price", "brand", "name", "number_of_inventory", "exp_date"]

        with open(f"{store_name}.csv") as file_reader:
            csv_reader = list(csv.reader(file_reader))

            for row in csv_reader:
                if csv_reader.index(row) == 0:
                    continue
                inventory_table.add_row(row)

        return inventory_table

    @staticmethod
    def search_goods(store_name):
        print("\n" + "\u2500" * 45 + " << SEARCH GOODS >> " + "\u2500" * 45 + "\n")

        store_reader = list(csv.reader(open(f"{store_name}.csv")))

        while True:
            flag = False

            brand_search_good = input("Please enter your desired brand: ")
            name_search_good = input("Please enter your desired name of good: ")

            for i in range(len(store_reader)):

                if str(list(store_reader)[i][3]) == name_search_good and \
                        str(list(store_reader)[i][2]) == brand_search_good:
                    print("The store you selected has the product you want.")
                    return brand_search_good, name_search_good

            if not flag:
                print("ATTENTION! This name does not exist!")
                return False

    @staticmethod
    def customer_invoices(date, user_name, store_name, brand, good_name, number, total_amount):

        invoice_dict = {"date": date, "store_name": store_name, "brand": brand, "good_name": good_name,
                        "number": number, "total_amount": total_amount}

        customer_invoice_file = FileHandler.FileHandler(f"{user_name}_invoice.csv")
        customer_invoice_file.add_to_file(invoice_dict)

        Manager.Manager.manager_invoices(date, store_name, user_name, brand, good_name, number, total_amount)

    @staticmethod
    def view_invoice(user_name):
        print("\n" + "\u2500" * 45 + " << CUSTOMER INVOICES >> " + "\u2500" * 45 + "\n")

        invoice_reader = list(csv.reader(open(f"{user_name}_invoice.csv")))

        my_table = PrettyTable()
        my_table.field_names = ["date", "store_name", "brand", "good_name", "number", "total_amount"]

        for i in invoice_reader:
            if invoice_reader.index(i) == 0:
                continue
            my_table.add_row(i)

        print(my_table)

    @staticmethod
    def confirm_show_pre_invoice(date, store_name, brand, good_name, number, total_amount):
        print("\n" + "\u2500" * 45 + " << SHOW PRE_INVOICE >> " + "\u2500" * 45 + "\n")

        my_table = PrettyTable()
        my_table.field_names = ["date", "store_name", "brand", "good_name", "number", "total_amount"]

        invoice_reader = [[date, store_name, brand, good_name, number, total_amount]]

        for i in invoice_reader:
            my_table.add_row(i)

        print(my_table)

        while True:
            confirm_cancel = input("Do you confirm the above invoice?(y: yea, n: no): ")

            if confirm_cancel.lower() == "y":
                return True

            elif confirm_cancel.lower() == "n":
                return False

            else:
                print("ERROR! Please choose between 'y' and 'n'.")
                continue

import csv

import re

import hashlib

import logging

import datetime

from prettytable import PrettyTable

import FileHandler

phone_regex = "(\+98|0)?9\d{9}"

pass_word_regex = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"


def password_hashing(password):
    hashed_password = hashlib.sha256(password.encode())
    return hashed_password.hexdigest()


class Customer:
    def __init__(self, user_name, pass_word):
        self.user_name = user_name
        self.pass_word = password_hashing(pass_word)

        customer_dict = self.__dict__

        file = FileHandler.FileHandler("Customer.csv")
        file.add_to_file(customer_dict)

    @classmethod
    def register(cls):

        print("\n" + "\u2500" * 35 + " << REGISTER >> " + "\u2500" * 35 + "\n")

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
        print("\n" + "\u2500" * 35 + " << SIGN IN >> " + "\u2500" * 35 + "\n")

        user_name = input("Please enter your USER NAME: ")
        pass_word = input("Please enter your PASS WORD: ")

        flag = False

        with open("Customer.csv") as file_reader:
            reader = csv.reader(file_reader)
            check = list(reader)

            for i in range(len(check)):
                if user_name == check[i][0] and password_hashing(pass_word) == check[i][1]:
                    print(f"\n{user_name} has successfully signed in.")

                    logging.basicConfig(level=logging.INFO, filename="sign_in_customer.log", filemode="a",
                                        format='%(name)s - %(levelname)s - %(message)s')
                    logging.info(f"{user_name} signed in / date_time -> {datetime.datetime.now()}")

                    return user_name

        if not flag:
            print("\nWARNING! User name or password is wrong!")

            logging.basicConfig(level=logging.WARNING, filename="failed_log_in_customer.log", filemode="a",
                                format='%(name)s - %(levelname)s - %(message)s')
            logging.warning(f"{user_name} failed to log in / date_time -> {datetime.datetime.now()}")

            return False

    @staticmethod
    def view():
        print("\n" + "\u2500" * 35 + " << CUSTOMER LIST >> " + "\u2500" * 35 + "\n")

        customer_table = PrettyTable()
        customer_table.field_names = ["user_name", "pass_word"]

        with open("customer.csv") as file_reader:
            csv_reader = list(csv.reader(file_reader))

            for row in csv_reader:
                if csv_reader.index(row) == 0:
                    continue
                customer_table.add_row(row)

        print(customer_table)

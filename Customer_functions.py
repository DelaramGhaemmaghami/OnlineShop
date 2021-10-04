import hashlib
import csv


def password_hashing(password):
    hashed_password = hashlib.sha256(password.encode())
    return hashed_password.hexdigest()


def wanna_buy(desired_store_name=None):
    while True:
        buy = input("Do you wanna buy something?(y: yes, n: no): ")

        store_reader = list(csv.reader(open("existed_store.csv")))

        if buy.lower() == "y":

            while True:
                flag = False

                if desired_store_name is None:
                    desired_store_name = input("Please enter the name of the store: ")

                for i in range(len(store_reader)):
                    if str(list(store_reader)[i][0]) == desired_store_name:
                        return desired_store_name

                if not flag:
                    print("ATTENTION! It seems you entered the store name incorrectly, please enter again.")
                    continue

        elif buy.lower() == "n":
            return False

        else:
            print("ERROR! Please choose between 'y' or 'no'.")
            continue


def get_check_number():
    while True:
        required_amount = input("How many do you need?: ")

        if required_amount.isnumeric():
            return int(required_amount)

        else:
            print("\nINVALID INPUT! Please enter a number.")
            continue


def is_blocked(store_name, user_name):
    block_file_reader = list(csv.reader(open(f"{store_name}_blocked_users.csv")))

    flag = False

    for i in range(len(block_file_reader)):
        if block_file_reader[i][1] == user_name:
            print(f"ATTENTION! You can't buy from {store_name}, because you've been blocked.")
            return True

    if not flag:
        return False

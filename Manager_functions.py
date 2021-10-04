import logging
import hashlib
import datetime
import csv


def password_hashing(password):
    hashed_password = hashlib.sha256(password.encode())
    return hashed_password.hexdigest()


def get_and_check_open():
    while True:
        start_time = input("When does the store open?: ")

        if start_time.isnumeric() and int(start_time) in range(0, 25):
            return int(start_time)

        else:
            print("\nERROR! Please enter a number between 0 and 24.")

            logging.basicConfig(level=logging.ERROR, filename="errors.log", filemode="a",
                                format='%(name)s - %(levelname)s - %(message)s')
            logging.error(f"""Some one entered an invalid input /"""
                          f"""date_time -> {datetime.datetime.now()}""")

            continue


def get_and_check_close():
    while True:
        close_time = input("When does the store close?: ")

        if close_time.isnumeric() and int(close_time) in range(0, 25):
            return int(close_time)

        else:
            print("\nERROR! Please enter a number between 0 and 24.")

            logging.basicConfig(level=logging.ERROR, filename="errors.log", filemode="a",
                                format='%(name)s - %(levelname)s - %(message)s')
            logging.error(f"""Some one entered an invalid input /"""
                          f"""date_time -> {datetime.datetime.now()}""")

            continue


def find_store_name(user_name):
    manager_reader = list(csv.reader(open("Manager.csv")))

    for i in range(len(manager_reader)):

        if manager_reader[i][0] == user_name:
            return manager_reader[i][2]
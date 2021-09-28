import csv
import os
from csv import DictWriter


class FileHandler:
    def __init__(self, file_path='data.csv'):
        self.file_path = file_path

    def read_file(self):
        with open(self.file_path, 'r') as myfile:
            reader = csv.DictReader(myfile)
            return list(reader)

    def add_to_file(self, new_value):
        if isinstance(new_value, dict):
            fields = new_value.keys()
            new_value = [new_value]
        elif isinstance(new_value, list):
            fields = new_value[0].keys()

        with open(self.file_path, 'a', newline="") as myfile:
            writer = DictWriter(myfile, fieldnames=fields)

            if myfile.tell() == 0:
                writer.writeheader()

            writer.writerows(new_value)

    def overwrite(self, value):
        with open(self.file_path, 'w') as my_file:
            writer = DictWriter(my_file, fieldnames=value.keys())

            if my_file.tell() == 0:
                writer.writeheader()

            writer.writerow(value)

    def is_exist(self):
        if os.path.isfile(self.file_path):
            return True

        return False

    def is_empty(self):
        if os.path.getsize(self.file_path) == 0:
            return True

        return False

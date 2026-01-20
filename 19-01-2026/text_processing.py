"""Problem 8: Data Cleansing Pipeline for CSV Imports
A system imports CSV data from external vendors, but fields often contain embedded text noise.
Design a pipeline that:
Cleans textual fields

Validates values using regular expressions

Deduplicates records

Stores processed data in efficient in-memory structures

The solution should minimize repeated logic and include unit tests for different input scenarios."""


import re
import csv

class Text:

    @staticmethod
    def clean_text(value):
        """
        Cleans the given text input.

        Removes leading and trailing spaces
        Removes special characters except alphabets, numbers, '@', '.', '_', and spaces
        Converts None values to an empty string

        :param value: The input value to be cleaned
        :type value: str or None
        :return: Cleaned text string
        :rtype: str
        """
        if value is None:
            return ""
        value = value.strip()
        value = re.sub(r"[^a-zA-Z0-9@._\s]", "", value)
        return value

    @staticmethod
    def is_valid_email(email):
        """
        Validates an email address using a regular expression.

        :param email: Email address to validate
        :type email: str
        :return: True if email is valid, False otherwise
        :rtype: bool
        """
        pattern = r"^[a-zA-Z0-9._]+@[a-zA-Z0-9.]+\.[a-zA-Z]{2,}$"
        return bool(re.match(pattern, email))
    
    @staticmethod
    def is_valid_phone(phone):
        """
        Validates a phone number.

        Rules:
        Must be exactly 10 digits
        Must start with digits 6, 7, 8, or 9

        :param phone: Phone number to validate
        :type phone: str
        :return: True if phone number is valid, False otherwise
        :rtype: bool
        """
        pattern = r"^[6-9][0-9]{9}$"
        return bool(re.match(pattern, phone))
    
    @staticmethod
    def is_valid_age(age):

        """
        Validates an age value.

        Rules:
        Must be numeric
        Must be between 1 and 99

        :param age: Age value to validate
        :type age: str
        :return: True if age is valid, False otherwise
        :rtype: bool
        """
        return bool(age.isdigit() and 0 < int(age) < 100)

    @staticmethod
    def load_from_csv(file_name):
        """
        Load the data from csv file
        Validation checks include:
        Valid email format
        Valid phone number
        Valid age range

        Invalid records are skipped.

        :param file_name: Name of the input CSV file
        :type file_name: str
        :return: List of valid rows extracted from the CSV
        :rtype: list of dict
        """
        rows = []

        with open(file_name, "r") as csv_file:
            csv_reader = csv.DictReader(csv_file)

            for line in csv_reader:
                email = Text.clean_text(line["email"])
                phone = Text.clean_text(line["phonenumber"])
                age = Text.clean_text(line["age"])
        
                if not Text.is_valid_email(email):
                    continue
                if not Text.is_valid_phone(phone):
                    continue
                if not Text.is_valid_age(age):
                    continue

                rows.append({
                    "email": email,
                    "phone": phone,
                    "age": age
                })

                with open("output.csv", "w") as outfile:
                    writer = csv.DictWriter(outfile, fieldnames=["email","phone","age"])
                    writer.writeheader()
                    writer.writerows(rows)

Text.load_from_csv("file.csv")

# DaviansWallet; In our virtual-wallet we trust.
import hashlib
import time
import datetime
import os
import sys

def introduction():
    print("Hey there! to make your account type in the amount of your virtual-currency")
    cryptoCurrency = int(input("Type in the amount of your virtual-currency: "))
    # The users information will displayed in a text file

    # Text files will be a major contributor to this whole program, mainly it displays
    # the users personal information adn transaction records

    name = input("Type in your name: ")
    age = int(input("Type in your age: "))
    BM = int(input("Type in your birthmonth: "))
    BDT = int(input("Type in your birthdate: "))
    BY = int(input("Type in your birthyear: "))
    Birthday = f"{BM}/{BDT}/{BY}"

    # The main text file program
    # The creating process
    userFile = open("identiy.txt", "w+")
    # The writing process
    userFile.write(f"Name:{name} \
                     Age: {age} \
                     Birthday: {Birthday}")
    useFile.close()

class Block:
    def __init__(self, previous_transactions, timestamp, data):
        self.previous_transactions = self.previous_transactions()
        self.timestamp = datetime.datetime.now()
        self.data = data
        self.cryptocurrency = cryptocurrency
        # The hash converter
        self.hash = self.get_hash() # Create a function
        self.payments = self.paid_items() # Create a function
        self.personal_information = self.personal_information()
        self.open_file = self.open_file()

        # To secure any transaction made
        def get_hash(self):
            hash_convert = (str(timestapm)+str(previous_transations)+str(data))
            # Depending on the transactio preference...
            private_transaction = hashlib.sha256(hash_convert).hexdigest()
            public_transaction = hashlib.sha256(private_transaction).hexdigest()
            for private_transaction in public_transaction(True):
                if not private_transaction(True):
                    # When it is not a private transaction, it returns the value of the time in hexidecimalz
                    timing = (str(timestamp)+str(previous_transaction)).datetime.datetime.now()
                    timing_transaction = hashlib.sha256(timing).hexdigest()
                    return timing_transaction
                elif private_transaction(True) != False:
                    # Type in the code, today
                    pass

        def payments(self, i):
            for i in payments:
                if i == datetime.datetime.now():
                    userInput = input("Please type in your current purchase: ")
                    price = int(input("Type in the price: "))
                    return hashlib.sha256(userInput+str(price)+str(datetime.datetime.now())).hexdigest() # For securing purposes
                else:
                    return None

        def personal_information(self):
            def PersInfo():
                editAccess = input("Do you edit your personal info? ")
                if editAccess == "yes" or editAccess == "Yes" or esitAccess == "y":
                    userFile = open("identity.txt", "w+")
                    edit = input("What do you want to edit? ")
                    if edit == "name":
                        userfile = open("identity.txt", "w+")
                        for edit in userFile:
                            # Type in the code, today
                            pass
                    elif edit == "birthday":
                        DMY = input("Year, month or day: ")
                        if DMY == "year" or DMY == "Year" or DMY == "YEAR":
                            yearEdit = int(input("Type in your updated year: "))
                            userFile = open("identity.txt", "w+")
                            userFile.read("identity.txt", "r")
                            for userFile in range(True):
                                return userFile.write(f"{month}/{date}/{yearEdit}")
                        elif DMY == "Month" or DMY == "month" or DMY == "YEAR":
                            monthEdit = input("Type in your updated month: ")
                            userFile = open("identity.txt", "w+")
                            userFile.read("identity.txt", "r")
                            for userFile in range(True):
                                return userFile.write(f"{monthEdit}/{date}/{year}")
                        elif DMY == "Date" or DMY == "DATE" or DMY == "date":
                            dateEdit = int(input("Type in your updated date: "))
                            userFile = open("identity.txt", "w+")
                            userFile.read("identity.txt", "r")
                            for userFile in range(True):
                                return userFile.write(f"{month}/{dateEdit}/{year}")
                    elif edit == "transaction amount" or edit == "virtual-money":
                        # Type in the code, today 
                        pass
                    else:
                        return False
        def previous_transactions(self):
            # Type in the code...
            pass

        def open_file(self):
            # Type in the code...
            pass
# In addition, another class will be implemented as a summary to previous class
class Blockchain(Block):
    def __init__(self, data):
        self.data = data
        # The function variables
        self.hashEncryption = self.hashEncryption()
        def hashEncryption(self):
            # Type in the code...
            pass

# Davian's Wallet; In our virtual-wallet we trust.
import hashlib
import time
import datetime
import random
import os
import sys
import json

from datetime import datetime
from hashlib import sha256
from time import time

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
    userFile = open("identity.txt", "w+")
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
        self.error = self.error()

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
                    return False

        def payments(self):
            for i in payments:
                if i == datetime.datetime.now():
                    userInput = input("Please type in your current purchase: ")
                    price = int(input("Type in the price: "))
                    return hashlib.sha256(userInput+str(price)+str(datetime.datetime.now())).hexdigest() and f"{userInput} was purchased successfuly" # For securing purposes
                else:
                    return None

        def transaction(self):
            # THe .txt identity file
            userFile = open("identity.txt", "w+") # Will take note of every transaction made
            # THe transaction process
            transaction_amount = int(input("How much money do you wish to transfer? "))
            virtual_money = int(input("Type in your current amount of virtual-money: "))
            receiver = input("Who would you want to gift: ")
            # Note: implement a "for loop", which is used for validation...
            if not transaction_amount(virtual_money):
                return f"Transaction may not be made"
            elif transaction_amount in virtual_money:
                transaction = hashlib.sha256(transaction_amount).hexdigest()
                msg = input("Type in a message for the receiver: ")
                return f"{msg}{transaction}{receiver}"
            else:
                return random.randint(False, None)

        def transaction_gift(transaction):
            purpose = input(f"What is your purpose upon giving {receiver} virtual-money: ")
            if purpose == "Birthday":
                amount = int(input("How much do you want to transfer? "))
                bday = input(f"When is your {receiver}'s birthday? ")
                date = datetime.strptime(bday)
                # Implementing time
                time.sleep(date)
                encryption = hashlib.sha256(str(bday)+str(purpose)+str(amount))
                # The time loop, for birthday purposes
                for time in bday(True):
                    if time.sleep(date) == bday:
                        result = True
                        return encryption and f"Your {amount} was transacted successfuly to {receiver}"
                    else:
                        return f"Your amount was unsuccesfuly transacted to {receiver}", False

            elif purpose == "Random act of kindness": # Would be inputted in other form, but ok...
                message = input("Type in a cheesy message: ")
                timing = int(input(datetime.strptime(f"When would you want {receiver} to receive the virtual-money?")))
                amount = int(input("How much would you want to give: "))
                try:
                    if datetime.datetime.now(True) == timing(True):
                        result1 = hashlib.sha256(message).hexdigest("utf-8")
                        result2 = hashlib.sha256(timing).hexdigest("utf-8")
                        result3 = hashlib.sha256(amount).hexdigest("utf-8")
                        encrypted = str(result1) + str(result2) + str(result3)
                        # Take note of the transaction, in the .txt file
                        userFile = open("identity.txt", "r")
                        userFile.write("Transaction: " + str() + str() + str())
                        return encrypted
                # A simple block function error.
                except(False):
                    print(f"{message}{timing}{amount} is invalid, please try again")
                    print(False)
            else:
                return False or None

        def personal_information(self):
            def PersInfo():
                editAccess = input("Do you edit your personal info? ")
                if editAccess == "yes" or editAccess == "Yes" or esitAccess == "y":
                    userFile = open("identity.txt", "w+")
                    edit = input("What do you want to edit? ")
                    if edit == "name":
                        nameUpdate = input("Type in your updated name: ")
                        userfile = open("identity.txt", "w+")
                        for edit in userFile:
                            userFile.write(f"Name:{nameUpdate}")
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
                        transactionUpdate = int(input("Type in your new amount of virtual-money: "))
                        print(hashlib.sha256(transactionUpdate).hexdigest())
                        transactionOption = input("Do you wish to create another transactions? ")
                        if transactionOption == "Yes" or transactionOption == "yes" or transactionOption == "YES":
                            toWho = input("Who would you want to create a transaction to?")
                            if toWho == "family" or toWho == "friend" or toWho == "colleague":
                                return self.transaction() and self.transaction_gift()
                    else:
                        return False

        def open_file(self):
            # Type in the code...
            pass

        def error(self):
            # Type in the code...
            pass

# In addition, another class will be implemented as a summary to previous class
class Blockchain(Block):
    def __init__(self, data):
        self.data = data
        # The function variables
        self.hashEncryption = self.hashEncryption()
        # A summary function, watch this video as a reminder to summarize "https://www.youtube.com/watch?v=b81Ib_oYbFk"
        def hashEncryption(self):
            encrypted = hashlib.sha256(Block)
            encrypted.updated(Block)
            for Blockchain in Block(True):
                encryption = str(get_hash().encode("utf-8")) + str(payments().encode("utf-8")) + str(personal_information().encode("utf-8"))
                return encryption
            else:
                return False

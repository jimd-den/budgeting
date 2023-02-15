"""
This is a running balance sheet application,
allows you to place in your income and helps you ...
track how close you are to breaking even and reaching your goals

add_transaction:


"""

import random
import bud_technical
import sys
from datetime import datetime, date, time, timezone
import time

## our main object is the transaction. Every Bill is a transaction, income is a transaction.


class Transaction:
    def __init__(self, transaction_id, amount, date, reason, transaction_type):
        self.transaction_id = transaction_id
        self.amount = amount
        self.date = date
        self.reason =  reason
        self.transaction_type = transaction_type


def remove_transaction():
    print("takes the id of the transaction")

def add_transaction():
    date = bud_technical.numeric_input("Date: ", 
                         "Please refer to calendar for numeric date:")
    amount = bud_technical.numeric_input("Amount: ",
                           "Please enter a dollar amount")
    transaction_type = bud_technical.numeric_input("income(1) or expense(0): ",
                                     "Please enter a 1 or a 0")
    reason = input("reason: ")
    
    buffer_transaction = Transaction(random.randint(0,3000),
                                     amount,
                                     date,
                                     reason,
                                     transaction_type)
    if transaction_type == 0:
        buffer_transaction.amount = 0 - buffer_transaction.amount
    transaction_tuple = (buffer_transaction.amount,
                         buffer_transaction.date,
                         buffer_transaction.reason)
    for i in transaction_tuple:
        print(i)
    insert_trans = bud_technical.insert_transaction(transaction_tuple)
    print("logged record number: ", insert_trans)
    

if __name__ == "__main__":
    ## DEBUG PURPOSE ##
    args = sys.argv
    for i, arg in enumerate(args):
        print(f"Argument {i:>6}: {arg}")
    ## DEBUG PURPOSE ##
    bud_technical.print_day()

    if len(args) > 1:
        match args[1]:
            case "--add_transaction":
                add_transaction()
            case "--remove_transaction":
               remove_transaction()
            case "--show_snapshot":
                show_snapshot()
            case "--create_db":
                bud_technical.create_database()

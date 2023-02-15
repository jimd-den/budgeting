"""
This is a running balance sheet application,
allows you to place in your income and helps you ...
track how close you are to breaking even and reaching your goals

add_transaction:


"""

import transaction_manager
import bud_technical
import sys

## our main object is the transaction. Every Bill is a transaction, income is a transaction.


    

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
               transaction_manager.add_transaction()
            case "--remove_transaction":
               transaction_manager.remove_transaction()
            case "--show_snapshot":
               transaction_manager.show_snapshot()
            case "--create_db":
                transaction_manager.db_init()

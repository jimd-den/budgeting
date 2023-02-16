import bud_technical

## Transaction Object Main Objective
class Transaction:
    def __init__(self, amount, date, reason, transaction_type):
        self.amount = amount
        self.date = date
        self.reason =  reason
        self.transaction_type = transaction_type

def db_init():
    bud_technical.create_database()


def remove_transaction():
    print("takes the id of the transaction")

def add_transaction():
    date = bud_technical.numeric_input("Date: ","Please refer to calendar for numeric date:")
    amount = bud_technical.numeric_input("Amount: ", "Please enter a dollar amount")
    transaction_type = bud_technical.numeric_input("income(1) or expense(0): ", "Please enter a 1 or a 0")
    reason = input("reason: ")

    buffer_transaction = Transaction(amount, date, reason,transaction_type)

    if transaction_type == 0:
        buffer_transaction.amount = 0 - buffer_transaction.amount

    transaction_tuple = (buffer_transaction.amount,
                         buffer_transaction.date,
                         buffer_transaction.reason)


    insert_trans = bud_technical.insert_transaction(transaction_tuple)
    
    print("logged record number: ", insert_trans)

## get transactions, parse to readable format
def list_transaction():
    print("LISTING TRANSACTION PLACEHOLDER")
    transaction_raw = bud_technical.get_items_from_db()
    for i in transaction_raw:
        print("Amount: ", i[1], "Date: ", i[2], "Reason: ", i[3])
        print("--------------------------------------------------")

def remove_transaction():
    list_transaction()
    transaction_choice = numeric_input("Which transaction: ", "Please enter a number.")


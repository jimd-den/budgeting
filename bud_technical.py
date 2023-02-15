import datetime
import sqlite3
import time


connection_obj = sqlite3.connect("budget_ledger.db")
cursor_obj = connection_obj.cursor()

def create_database():


    cursor_obj.execute("DROP TABLE IF EXISTS balance") ##don't need

    table = """ CREATE TABLE balance (
                transact_id INTEGER PRIMARY KEY,
                transact_amt INT NOT NULL,
                transact_date INT NOT NULL,
                transact_reas VARCHAR(255));
            """
    cursor_obj.execute(table)

    connection_obj.close()
    print("db initialized")

def insert_transaction(transaction_tuple):
    sql = '''INSERT INTO balance(transact_amt,transact_date,transact_reas)
             VALUES(?,?,?)'''
    cursor_obj.execute(sql, transaction_tuple)
    connection_obj.commit()
    return cursor_obj.lastrowid




def numeric_input(msg, error_msg):
    while True: 
        try: 
            raw_in = int(input(msg))
            return raw_in
            break
        except ValueError:
            print(error_msg)

def print_day():
    SEC_IN_DAY = 84600
    date_today = datetime.datetime.now()
    unix_time = time.mktime(date_today.timetuple())
    unix_day = unix_time / SEC_IN_DAY

    print("Date: ", date_today)
    print("Unix Day: ", int(unix_day))

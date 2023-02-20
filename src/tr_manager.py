import sqlite3


db_connection =  sqlite3.connect("bgt_fix.db")

def create_db_table():
    db_cursor = db_connection.cursor()
    sql_drop = "DROP TABLE IF EXISTS balance_sheet"
    db_cursor.execute(sql_drop)
    sql = '''CREATE TABLE  balance_sheet( b_id INT PRIMARY KEY,
                                        b_amt INT,
                                        b_date INT,
                                        b_reason STRING);
           '''
    db_cursor.execute(sql)
    print("table initialized")

def add_transaction(x):
    db_cursor = db_connection.cursor()

    data = (
        {"amt": x.amount, "dt": x.date, "reas": x.reason}
        )
    db_cursor.execute("INSERT INTO balance_sheet(b_amt,b_date, b_reason) VALUES (:amt, :dt ,:reas)", data)
    db_connection.commit()
    print(db_cursor.lastrowid)

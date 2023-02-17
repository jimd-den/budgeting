import sys
import argparse

## Main Object
class Transaction:
    def __init__(self, amount, date, reason):
        self.amount = amount
        self.date = date
        self.reason = reason
    def __str__(self):
        return f"Amount: {self.amount} Date: {self.date} Reason: {self.reason}"


## Check input format 3 variables separated by commas
def transaction_parse(string):
    incorrect_string_format = ('''
                            format = dbt_ctr -a [amount_number],[days_ahead],[reason]
                            ''')
    tr_raw = [x.strip() for x in string.split(',')]
    if len(tr_raw) == 3:
        try:
            amt_raw = int(tr_raw[0])
        except:
            print(incorrect_string_format)
            raise TypeError
        try:
            date_raw = int(tr_raw[1])
        except:
            print(incorrect_string_format)
            raise TypeError
        finally:
            reason_raw = tr_raw[2]
            buff_tr = Transaction(amt_raw, date_raw, reason_raw)
            return buff_tr

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
                        prog = "dbt_clt",
                        description = "show's you your dystopian finances",
                        epilog = "good luck")
    parser.add_argument('-a', '--add', type=transaction_parse)
    parser.add_argument('-r', '--remove')
    parser.add_argument('-s', '--show')
    args = parser.parse_args()
    if args.add != 0:
        print(args.add)
    print("##DEBUG##\n", args, "\n##DEBUG##")

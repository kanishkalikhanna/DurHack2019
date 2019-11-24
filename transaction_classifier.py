# Author: Mohamed Hammeda
import csv

class Transaction:

    def __init__(self, transaction_id, account_id, amount, necessity, accounts, group, month):

        self.id = transaction_id
        self.amount = float(amount)
        self.account_id = account_id
        self.necessity = float(necessity)
        self.month = month

        account = accounts[account_id]
        multiplier = 100 / (float(necessity) + 1)
        fraction = 0

        if group == "grocery" or account == "fine dining" or account == "fast food":
            fraction = (10 * float(amount)) / account.get_ideal_food_expenditure()

        elif group == "rent" or group == "utility bills":
            fraction = (10 * float(amount)) / account.get_ideal_accommodation_expenditure()

        elif group == "travelling" or group == "gym" or group == "movies":
            fraction = (10 * float(amount)) / account.get_ideal_leisure_expenditure()

        smart_score = multiplier * fraction

        self.smart_score = smart_score

    def get_account_id(self):
        return self.account_id

    def get_smart_score(self):
        return self.smart_score


def scan_csv(file_name, transactions, accounts, accounts_smart_scores):

    with open(file_name) as file:
        current_id = 0

        reader = csv.reader(file)

        next(reader, None)

        for row in reader:
            transaction_id = current_id
            current_id += 1
            account_id = row[0]
            month = row[1]
            necessity = row[2]
            group = row[3]
            amount = row[4]

            transactions[transaction_id] = Transaction(transaction_id, account_id, amount, necessity, accounts, group,
                                                       month)

            transaction = transactions[transaction_id]

            if account_id in accounts_smart_scores.keys():
                accounts_smart_scores[account_id].append(transaction.get_smart_score())
            else:
                accounts_smart_scores[account_id] = [transaction.get_smart_score()]

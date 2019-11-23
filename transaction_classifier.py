# Author: Mohamed Hammeda
import csv


class Transaction:

    def __init__(self, transaction_id, account_id, amount, necessity, accounts, group):

        self.id = transaction_id
        self.amount = amount
        self.account_id = account_id
        self.necessity = necessity

        account = accounts[account_id]
        multiplier = 100 / (necessity + 1)
        fraction = 0

        if group == "grocery" or account == "fine dining" or account == "fast food":
            fraction = (10 * amount) / account.get_ideal_food_expenditure()

        elif group == "rent" or group == "utility bills":
            fraction = (10 * amount) / account.get_ideal_accommodation_expenditure()

        elif group == "travelling" or group == "gym" or group == "movies":
            fraction = (10 * amount) / account.get_ideal_leisure_expenditure()

        smart_score = multiplier * fraction

        self.smart_score = smart_score

    def get_account_id(self):
        return self.account_id

    def get_smart_sore(self):
        return self.smart_score


def scan_csv(file_name, transactions, accounts_smart_scores):

    with open(file_name) as file:

        reader = csv.reader(file)

        next(reader, None)

        for row in reader:

            transactions[transaction_id] = Transaction(transaction_id, account_id, amount, necessity)

            if account_id in accounts_smart_scores:
                accounts_smart_scores[account_id].append(transactions[transaction_id].get_smart_score)
            else:
                accounts_smart_scores[account_id] = [transactions[transaction_id].get_smart_score]




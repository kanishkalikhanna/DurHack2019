# Author: Mohamed Hammeda
import csv
import statistics

class Transaction:

    def __init__(self, transaction_id, account_id, amount, necessity, people):

        self.id = transaction_id
        self.amount = amount
        self.accountId = account_id
        self.necessity = necessity
        self.ideal_smart_score = calculateSmartScore(people, account_id, amount, necessity)


    def calculateSmartScore(self, accounts, account_id, amount, necessity, group):
        account = accounts[account_id]
        multiplier = 100 / (necessity + 1)


        if group == "":
            fraction = (10 * amount) /

        elif group == "":
            fraction = (10 * amount) /

        elif group == "":
            fraction = (10 * amount) /

        elif group == "":
            fraction = (10 * amount) /

        elif group == "":
            fraction = (10 * amount) /

        smartScore = multiplier * fraction

        return smartScore

def scan_csv(file_name, transactions):

    with open(file_name) as file:

        reader = csv.reader(file)

        next(reader, None)

        for row in reader:

            transactions[transaction_id] = Transaction(transaction_id, account_id, amount, necessity)


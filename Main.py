import transaction_classifier
import target_spend_generator
import os
from tkinter import *
os.system("python3 analysing_spending.py")

accounts = {}
transactions = {}
accounts_smart_scores = {}
accounts_overall_smart_score = {}

target_spend_generator.scan_csv("consumer_spending.csv", accounts)
transaction_classifier.scan_csv("transactions.csv", transactions, accounts, accounts_smart_scores)

for account_smart_scores in accounts_smart_scores:

    count = 0
    total_smart_score = float(0)

    for smart_score in accounts_smart_scores[account_smart_scores]:

        count += 1

        total_smart_score = total_smart_score + smart_score

    account_overall_smart_score = total_smart_score / count

    accounts_overall_smart_score[account_smart_scores] = account_overall_smart_score


root = Tk()
label = Label(root, text = "After analysing transaction data \n")
label.pack()
label.config(font=("Didot", 40))

for account in accounts_overall_smart_score:

    line = "Account: " + accounts[account].get_id() + " has overall smart score of: " + str(round(accounts_overall_smart_score[account],2))
    account_label = Label(root, text = line)
    account_label.pack()
    account_label.config(font = ("Didot", 20))
root.mainloop()
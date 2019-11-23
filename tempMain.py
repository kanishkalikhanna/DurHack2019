import transaction_classifier
import target_spend_generator

accounts = {}
accounts_smart_scores = {}
accounts_overall_smart_score = {}

target_spend_generator.scan_csv("consumer_spending", accounts)
transaction_classifier.scan_csv("", transactions, accounts_smart_scores)

for account_smart_scores in accounts_smart_scores:

    count = 0
    total_smart_score = 0

    for smart_score in accounts_smart_scores[account_smart_scores]:
        count += 1
        total_smart_score += smart_score

    account_overall_smart_score = total_smart_score / count

    accounts_overall_smart_score[account_smart_scores] = account_overall_smart_score


for account in account_overall_smart_score:
    print("Account: " + account.get_id() + " has overall smart score of: " + account_overall_smart_score[account])

# Author: Mohamed Hammeda
import csv
import statistics

class Account:

    def __init__(self, account_id):
        self.account_id = account_id
        self.number_months_active = 1
        self.total_income = 0
        self.expected_income = 0
        self.monthly_food_expenditure = []
        self.monthly_accommodation_expenditure = []
        self.monthly_leisure_expenditure = []
        self.ideal_food_expenditure = 0
        self.ideal_accommodation_expenditure = 0
        self.ideal_leisure_expenditure = 0

    def get_id(self):
        return self.account_id

    def get_ideal_food_expenditure(self):
        return self.ideal_food_expenditure

    def get_ideal_accommodation_expenditure(self):
        return self.ideal_accommodation_expenditure

    def get_ideal_leisure_expenditure(self):
        return self.ideal_leisure_expenditure

    def increment_number_months_active(self):
        self.number_months_active += 1

    def update_expected_income(self, month_income):
        self.total_income = self.total_income + month_income
        self.expected_income = self.total_income / self.number_months_active

    def update_ideal_food_expenditure(self, month_food_expenditure):
        self.monthly_food_expenditure.append(month_food_expenditure)
        self.ideal_food_expenditure = statistics.median_low(self.monthly_food_expenditure)

    def update_ideal_accommodation_expenditure(self, month_accommodation_expenditure):
        self.monthly_accommodation_expenditure.append(month_accommodation_expenditure)
        self.ideal_accommodation_expenditure = statistics.median_low(self.monthly_accommodation_expenditure)

    def update_ideal_leisure_expenditure(self, month_leisure_expenditure):
        self.monthly_leisure_expenditure.append(month_leisure_expenditure)
        self.ideal_leisure_expenditure = statistics.median_low(self.monthly_leisure_expenditure)


def scan_csv(file_name, accounts):

    with open(file_name) as file:

        reader = csv.reader(file)

        next(reader, None)

        for row in reader:

            row_id = row[0]
            row_income = row[2]
            row_food_expenditure = row[3]
            row_accommodation_expenditure = row[4]
            row_leisure_expenditure = row[5]

            if row_id in accounts:
                person_to_manipulate = accounts[row_id]
                person_to_manipulate.increment_number_months_active()
                person_to_manipulate.update_expected_income(float(row_income))
                person_to_manipulate.update_ideal_food_expenditure(float(row_food_expenditure))
                person_to_manipulate.update_ideal_accommodation_expenditure(float(row_accommodation_expenditure))
                person_to_manipulate.update_ideal_leisure_expenditure(float(row_leisure_expenditure))

            else:
                accounts[row_id] = Account(row_id)
                person_to_manipulate = accounts[row_id]
                person_to_manipulate.update_expected_income(float(row_income))
                person_to_manipulate.update_ideal_food_expenditure(float(row_food_expenditure))
                person_to_manipulate.update_ideal_accommodation_expenditure(float(row_accommodation_expenditure))
                person_to_manipulate.update_ideal_leisure_expenditure(float(row_leisure_expenditure))


def print_each_accounts(accounts):

    for a in accounts.values():
        print("Account " + a.get_id())
        print("Ideal food expenditure: " + str(a.get_ideal_food_expenditure()))
        print("Ideal accommodation expenditure: " + str(a.get_ideal_accommodation_expenditure()))
        print("Ideal Leisure expenditure: " + str(a.get_ideal_leisure_expenditure()))
import random

food_sub_types = ["grocery", "fine dining", "fast food"]
accommodation_sub_type = ["rent", "utilities"]
leisure_sub_type = ["travelling", "movies", "gym"]


def generate_data(file_name):

    monthly_spending = open(file_name)
    make_transactions = open("transactions.csv", "w")
    make_transactions.write("ID,MONTH,NECESSITY,SUB TYPE,AMOUNT")
    i = 0
    for line in monthly_spending:
        if i > 0:
            parameters = line.split(',')

            total_food_expenditure = float(parameters[3])
            write_specific_transactions(0, make_transactions, parameters, total_food_expenditure, food_sub_types)

            create_accommodation_transactions(make_transactions, parameters)

            total_leisure_expenditure = float(parameters[5])
            write_specific_transactions(0, make_transactions, parameters, total_leisure_expenditure, leisure_sub_type)
        i += 1


def create_accommodation_transactions(make_transactions, parameters):
    total_accommodation_expenditure = float(parameters[4])
    proportion_on_rent = (random.randint(70, 90)) / 100
    proportion_on_utilities = (100 - proportion_on_rent) / 100
    necessity = str(random.randint(0, 100))
    make_transactions.write("\n" + parameters[0] + "," + parameters[1] + "," + necessity + "," +
                            accommodation_sub_type[0] + "," + str(
        round(total_accommodation_expenditure * proportion_on_rent, 2)))
    make_transactions.write("\n" + parameters[0] + "," + parameters[1] + "," + necessity + "," +
                            accommodation_sub_type[1] + "," +
                            str(round(total_accommodation_expenditure * proportion_on_utilities, 2)))


def write_specific_transactions(amount_spent, make_transactions, parameters, total_type_expenditure, sub_type_array):
    while amount_spent < total_type_expenditure:
        amount_on_current_transaction = min(total_type_expenditure - amount_spent,
                                            random.randint(int(total_type_expenditure / 10), int(total_type_expenditure / 4)))
        amount_spent += amount_on_current_transaction
        sub_type = random.randint(0, len(sub_type_array) - 1)
        necessity = str(random.randint(0, 100))
        make_transactions.write("\n" + parameters[0] + "," + parameters[1] + "," + necessity + "," +
                                sub_type_array[sub_type] + "," + str(round(amount_on_current_transaction,2)))


generate_data("consumer_spending.csv")

import random

def data_generator(file_name, number_of_consumers):

    random.seed(100)
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
              "November", "December"]
    consumer_spending = open(file_name, "w")

    consumer_spending.write("ID,MONTH,INCOME,FOOD EXPENDITURE,ACCOMMODATION EXPENDITURE,LEISURE EXPENDITURE, "
                            "TOTAL EXPENDITURE")

    for i in range(1, number_of_consumers + 1):

        income = random.randint(1000, 4000)
        orig_perc_leisure = random.randint(5, 50) / 100
        orig_perc_accommodation = random.randint(20, 50) / 100
        orig_perc_food = random.randint(10, 20) / 100

        for j in months:

            perc_leisure = orig_perc_leisure + (random.randint(-5, 5) / 100)
            perc_accomodation = orig_perc_accommodation + (random.randint(-5, 5) / 100)
            perc_food = orig_perc_food + (random.randint(-5, 5) / 100)

            food_expenditure = round(perc_food * income, 2)
            accommodation_expenditure = round(perc_accomodation * income, 2)
            leisure_expenditure = round(perc_leisure * income, 2)
            total_expenditure = round((perc_food + perc_leisure + perc_accomodation)*income,2)

            consumer_spending.write(
                "\n" + str(i) + "," + j + "," + str(income) + "," + str(food_expenditure) + "," +
                str(accommodation_expenditure) + "," + str(leisure_expenditure) + "," + str(total_expenditure))


data_generator("consumer_spending.csv", 5)

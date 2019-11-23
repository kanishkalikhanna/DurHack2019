import random


def data_generator(file_name, number_of_consumers):
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
              "November", "December"]
    consumer_spending = open(file_name, "w")

    consumer_spending.write("ID,MONTH,INCOME,FOOD EXPENDITURE, ACCOMMODATION EXPENDITURE, LEISURE EXPENDITURE")

    for i in range(1, number_of_consumers + 1):

        income = random.randint(1000, 4000)
        orig_perc_leisure = random.randint(5, 50) / 100
        orig_perc_accomodation = random.randint(20, 50) / 100
        orig_perc_food = random.randint(10, 20) / 100

        for j in months:
            perc_leisure = orig_perc_leisure + (random.randint(-5, 5) / 100)
            perc_accomodation = orig_perc_accomodation + (random.randint(-5, 5) / 100)
            perc_food = orig_perc_food + (random.randint(-5, 5) / 100)

            consumer_spending.write(
                "\n" + str(i) + "," + j + "," + str(income) + "," + str(round(perc_food * income, 2)) + "," + str(
                    round(perc_accomodation * income, 2)) + "," + str(round(perc_leisure * income, 2)))


data_generator("consumer_spending.csv", 5)

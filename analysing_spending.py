import csv
from matplotlib.pylab import *

# Initialising empty arrays
user_id = []
months = []
income = []
food_exp = []
accom_exp = []
leisure_exp = []

months_ordered = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
                  "November", "December"]

# Adding each column to an array
try:
    with open("consumer_spending.csv") as csv_file:
        data = csv.reader(csv_file)
        header = next(data)
        data = csv.reader(csv_file, delimiter=',')
        for row in data:
            user_id.append(int(row[0]))
            income.append(int(row[2]))
            food_exp.append(float(row[3]))
            accom_exp.append(float(row[4]))
            leisure_exp.append(float(row[5]))
except FileNotFoundError:
    print("File not found")
    sys.exit(0)


def plot_for_each_person(person_id):
    income_for_person = []
    sum_each_month = []
    for person in range(len(user_id)):
        if user_id[person] == person_id:
            income_for_person.append(income[person])
            sum_each_month.append(food_exp[person] + accom_exp[person] + leisure_exp[person])

    y_min = min(sum_each_month)
    x_pos = sum_each_month.index(y_min)
    x_min = months_ordered[x_pos]
    plt.annotate(round(y_min, 2), xy=(x_min, y_min), xytext=(x_min, y_min + 5),
                 arrowprops=dict(facecolor='red', shrink=0.05), )
    plt.plot(months_ordered, sum_each_month)
    plt.plot(months_ordered, income_for_person)
    ylabel("£")
    xlabel("Months")
    plt.show()


for i in range(1, len(set(user_id)) + 1):
    plot_for_each_person(i)

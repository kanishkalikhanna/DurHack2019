import csv
import sys
from matplotlib.pylab import *
import numpy as np
import scipy as sp
import datetime as dt


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
            months.append(row[1])
            income.append(int(row[2]))
            food_exp.append(float(row[3]))
            accom_exp.append(float(row[4]))
            leisure_exp.append(float(row[5]))
except FileNotFoundError:
    print("File not found")
    sys.exit(0)


def sum_total_exp(person_wanted):
    s = 0
    for i in range(len(user_id)):
        if user_id[i] == person_wanted:
            s += food_exp[i] + accom_exp[i] + leisure_exp[i]
    return s


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
    plt.show()


# def savings_for_each_person(person_id):
#     savings_each_month = []
#     sum_each_month = []
#     for i in range(len(user_id)):
#         if user_id[i] == person_id:
#             sum_each_month.append(food_exp[i] + accom_exp[i] + leisure_exp[i])
#             calc = ((income[i] - sum_each_month[i]) / income[i])*100
#             savings_each_month.append(calc)
#     plt.plot(months_ordered, savings_each_month)
#     ylabel("£")
#     plt.show()


for i in range(1, len(set(user_id)) + 1):
    # sum_each_month(i)
    plot_for_each_person(i)
    # savings_for_each_person(i)

# def plot_data(y1, y2, type_of_graph):
#     # Plotting each graph, the trend lines and the point of crossover
#     plt.plot(array_lengths, y1, '.')
#     plt.plot(array_lengths, y2, '.')
#     plt.plot(array_lengths, 0.70 * nlogn_fit(array_lengths * (np.log2(array_lengths))))
#     plt.plot(array_lengths, n_squared_fit(array_lengths * array_lengths))
#     # Taken from stack overflow to find and plot the intersections of two graphs
#     # ref 3 in sources of report
#     idx = np.argwhere(np.diff(np.sign(y1 - y2)) != 0).reshape(-1) + 0  # Calculating where the intersection occurs
#     for i in range(len(idx)):
#         plt.plot((array_lengths[idx[i]] + array_lengths[idx[i] + 1]) / 2, (y1[idx[i]] + y1[idx[i] + 1]) / 2,
#                  'ko')  # Plotting the intersection as a black circle
#     xlabel("Array Length")
#     ylabel("Sort times (ns)")
#     title("Graph of " + type_of_graph + " sorting times vs array length")
#     legend(["Merge sort " + type_of_graph + " times (ns)", "Selection sort " + type_of_graph + " times (ns)",
#             "Merge Sort Trend line", "Selection Sort Trend line", "Intersection(s)"])
#     for i in range(len(idx)):
#         idx[i] = idx[i] + 1  # Adding 1 to find the actual intersection
#     print("Intersection(s) for " + type_of_graph + " times graph at x (array length) value(s)",
#           ', '.join(map(str, idx)))
#     plt.show()
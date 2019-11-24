import csv
from matplotlib.pylab import *
import matplotlib.style as style
from matplotlib.backends.backend_pdf import PdfPages
from fpdf import FPDF

style.use('bmh')
style.use('grayscale')

# Initialising empty arrays
user_id = []
months = []
income = []
food_exp = []
accom_exp = []
leisure_exp = []
id_expenditure_plot_map = {}
id_savings_plot_map = {}
figures = []

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

def plot_expenditure_for_each_person(person_id):

    income_for_person, sum_each_month = sum_different_expenditures(person_id)
    y_min = min(sum_each_month)
    x_pos = sum_each_month.index(y_min)
    x_min = months_ordered[x_pos]
    fig = plt.figure()
    plt.annotate(round(y_min, 2), xy=(x_min, y_min), xytext=(x_min, y_min + 5),
                 arrowprops=dict(facecolor='red', shrink=0.05))
    barplot = plt.bar(months_ordered, sum_each_month, color='cadetblue', figure = fig)
    barplot[x_pos].set_color('aqua')
    plt.plot(months_ordered, income_for_person, label="Income")
    plt.legend(loc="upper left")
    legend(["Income"])
    plt.xticks(rotation=30)
    ylabel("£", rotation=0)
    xlabel("Months")
    title("Monthly Total Expenditure and Income")
    figures.append(fig)
    plt.show()

def plot_savings_for_each_person(person_id):
    income_for_person, sum_each_month = sum_different_expenditures(person_id)
    savings = []
    for j in range(len(income_for_person)):
        savings.append(((income_for_person[j] - sum_each_month[j]) / income_for_person[j]) * 100)
    fig = plt.figure()
    plt.plot(months_ordered, savings, figure = fig)
    plt.xticks(rotation=30)
    ylabel("%", rotation = 0)
    title("Savings as % of Income")
    figures.append(fig)
    plt.show()

def sum_different_expenditures(person_id):
    income_for_person = []
    sum_each_month = []
    for person in range(len(user_id)):
        if user_id[person] == person_id:
            income_for_person.append(income[person])
            sum_each_month.append(food_exp[person] + accom_exp[person] + leisure_exp[person])
    return income_for_person, sum_each_month

for i in range(1, len(set(user_id)) + 1):
    plot_expenditure_for_each_person(i)
    plot_savings_for_each_person(i)

pdf = PdfPages("graphs.pdf")
fpdf = FPDF()
i = 0
for fig in figures:
    # if i%2 == 0:
    #     fpdf.add_page()
    #     fpdf.set_xy(0,0)
    #     fpdf.set_font("arial",'B', 30)
    #     fpdf.cell(txt = ("User " + str(i//2 + 1)))
    #     fpdf.output('graphs.pdf', 'F')
    fig.savefig(pdf, format = 'pdf')
    # i += 1
pdf.close()
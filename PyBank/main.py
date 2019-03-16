import os
import csv

# Path to collect data from the Resources folder
csvpath = os.path.join("..", "Resources", "Homework_03 - Python_PyBank_Resources_budget_data.csv")

# Open the CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

csv_reader_object.line_num
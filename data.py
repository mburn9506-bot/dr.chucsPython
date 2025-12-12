import csv


with open("data.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)
# to read file as dictionary extract the file line as dictonary
#++++++++++++++++++++++++++++++++++

with open("data.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
#extract lines from file as a list
#output:
# ['name', 'age', 'city']
# ['mike', '30', 'beirut']
# ['sara', '25', 'tripoli']

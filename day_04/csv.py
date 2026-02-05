import csv
students = [
    ["Name", "Age", "Grade"],
    ["John", "20", "A"],
    ["Jane", "22", "B"],
    ["Jack", "21", "C"],
]

# write
with open("students.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerows(students)

with open("students.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# read as dict
with open("students.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f"Name: {row['Name']}, Age: {row['Age']}, Grade: {row['Grade']}")

# write
family = [
    ["Iqbol", "Dilrabo", "Iftihorbek", "Farzonabonu", "Ismoilbek"],
    ["Iqbol", "Dilrabo", "Iftihorbek", "Farzonabonu", "Ismoilbek"],
    ["Iqbol", "Dilrabo", "Iftihorbek", "Farzonabonu", "Ismoilbek"],
]
# write
with open("students.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerows(family)

with open("students.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)
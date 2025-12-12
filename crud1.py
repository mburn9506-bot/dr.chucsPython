import csv

students = []

# ---------- LOAD FROM CSV (runs once at start) ----------
def load_from_csv():
    try:
        with open("students.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row:  # Avoid empty lines
                    name, age, grade = row
                    students.append({"name": name, "age": age, "grade": grade})
        print("Loaded existing students from CSV.\n")
    except FileNotFoundError:
        print("No CSV file found. Starting empty.\n")


# ---------- SAVE TO CSV ----------
def save_to_csv():
    with open("students.csv", "w", newline="") as file:
        writer = csv.writer(file)
        for s in students:
            writer.writerow([s["name"], s["age"], s["grade"]])
    print("Data saved to students.csv!\n")


# ---------- CRUD FUNCTIONS ----------
def create_student():
    name = input("Enter name: ")
    age = input("Enter age: ")
    grade = input("Enter grade: ")
    student = {"name": name, "age": age, "grade": grade}
    students.append(student)
    print("Student added successfully!\n")
    save_to_csv()

def read_students():
    if not students:
        print("No students found.\n")
    else:
        for i, student in enumerate(students):
            print(f"{i}. {student['name']} - Age: {student['age']} - Grade: {student['grade']}")
        print()

def update_student():
    read_students()
    index = int(input("Enter index of student to update: "))
    if 0 <= index < len(students):
        name = input("Enter new name: ")
        age = input("Enter new age: ")
        grade = input("Enter new grade: ")
        students[index] = {"name": name, "age": age, "grade": grade}
        print("Student updated!\n")
        save_to_csv()
    else:
        print("Invalid index.\n")

def delete_student():
    read_students()
    index = int(input("Enter index to delete: "))
    if 0 <= index < len(students):
        students.pop(index)
        print("Student deleted!\n")
        save_to_csv()
    else:
        print("Invalid index.\n")


# ---------- MAIN PROGRAM ----------
def main():
    load_from_csv()  # Load data when program starts

    while True:
        print("1. Create Student")
        print("2. Read Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Choose: ")

        if choice == "1":
            create_student()
        elif choice == "2":
            read_students()
        elif choice == "3":
            update_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.\n")


main()

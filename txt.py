import pickle

while True:
    print("\nMenu:")
    print("1. Add a student")
    print("2. Search for a student")
    print("3. Display all students")
    print("4. Modify the details of a student")
    print("5. Delete a student")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        roll_no = int(input("Enter roll number: "))
        name = input("Enter student name: ")
        grade = input("Enter grade: ")
        division = input("Enter division: ")

        students=[roll_no, name, grade, division]

        with open("students.dat", "wb") as f:
            pickle.dump(students, f)

    elif choice == 2:
        roll_no = int(input("Enter roll number to search: "))

        with open("students.dat", "rb") as f:
            students = pickle.load(f)

        for student in students:
            if student.roll_no == roll_no:
                print(student)
                break
        else:
            print("Student not found")

    elif choice == 3:
        with open("students.dat", "rb") as f:
            students = pickle.load(f)

        for student in students:
            print(student)

    elif choice == 4:
        roll_no = int(input("Enter roll number to modify: "))

        with open("students.dat", "rb") as f:
            students = pickle.load(f)

        for student in students:
            if student.roll_no == roll_no:
                print("Student found: ", student)
                print("Enter new details")

                name = input("Enter student name: ")
                grade = input("Enter grade: ")
                division = input("Enter division: ")

                student.name = name
                student.grade = grade
                student.division = division

                with open("students.dat", "wb") as f:
                    pickle.dump(students, f)

                break
        else:
            print("Student not found")

    elif choice == 5:
        roll_no = int(input("Enter roll number to delete: "))

        with open("students.dat", "rb") as f:
            students = pickle.load(f)

        for i, student in enumerate(students):
            if student.roll_no == roll_no:
                del students[i]

                with open("students.dat", "wb") as f:
                    pickle.dump(students, f)

                break
        else:
            print("Student not found")

    elif choice == 6:
        break

    else:
        print("Invalid choice. Please try again.")
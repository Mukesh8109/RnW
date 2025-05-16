students_details = []

print("\n")

print("Welcome to the Student Data Organizer")
print("\n")
print("Select an option: ")
while True:
    print("1. add student")
    print("2. Display All Student")
    print("3. update Student Information")
    print("4. Delete Student")
    print("5. Display Subject Offered")
    print("6. Exit")
    
    choice = input("enter  your choice: ")

    match choice:
    #add
        case "1":
            

            student_id = input(" student id: ")
            name = input(str("name: "))
            age = input("age: ")
            grade = input("grade: ")
            date_of_birth = input("date of birth (DD-MM-yyyy)")
            subject = input("subject (comma-separated): ")

            identity = (student_id,dob)

            students_data = { 

                "identity":identity,
                "name":name,
                "age":age,
                "grade":grade,
                "subject":subject
            }

            students_details.append(students_data)

            print("student added succesfully!")

        case "2":
        #display
            if not students_details:
                print("no record found!!")
            else:
                print("\n---students records---")
            
                for student in students_details:
                    sid , dob = identity
                    print(f"Student id {sid} | name: {student['name']} | age: {student['age']} | grade: {student['grade']} ")
                    print("subject: ",student['subject'])
                    print("-"*50)

        case "3":
         #replace 

            sid = input("enter student id: ")
            for student in students_details:
                if student["identity"] [0] == sid:
                    student["name"] = str(input("enter student name: "))
                    student["age"] = int(input("enter age: "))
                    student["grade"] = input("enter new grade: ")
                    student["subject"] = input("enter new subject")

                    print("studented updated!!")
                    break
                else:
                    print("student id not found..")

        case "4":
        #delete
            sid = input("enter student id: ")
            for i , student in enumerate[sid]:
                if student["identity"] [0]== sid:
                    del student[i]
                    print("deleted successfully")
                break
            else:
                print("student not found")

        case "5":
        #subject offered

            subject_set = set()

            for student in students_details:
                subject_set.update([subject])

            print("subject offered")
            for sub in sorted(subject_set):
                print("-",sub)

        case "5":
            print("thanku for your support !!")
            break

        case __:
            print("invalid case :")
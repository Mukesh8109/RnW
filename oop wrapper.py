print("python OOP project : Employee management system")

while True:
    print("1. choose an operation")
    print("2. create an empolyee")
    print("3. create a manager")
    print("4. show details")
    print("5. compare salaries")
    print("6. exit")

    choice=input("enter your choice : ")

    match choice:

        case "1":
            class person:
                name = None
                age = None

            p1=person()

            p1.name=input("enter the name :")       
            p1.age=input("enter the age :")
            print(f"person created with age = {p1.age}  and name = {p1.name}" )
            
            print("--choose another option--")

        case "2":

            class Employee:
                
                name = None 
                salary = None
                age = None
                employee_id =None

            e1=Employee()   

            e1.name=input("enter name :")
            e1.salary=int(input("enter salary :"))
            e1.age=int(input("enter age :"))
            e1.employee_id=int(input("employee id :"))

            print(f" Employee created with Name: {e1.name}  Salary: {e1.salary} age = {e1.age} employee_id = {e1.employee_id}")

            print("--choose another option--")
        case "3":

            class manager:
                name=None
                age=None
                salary=None
                department=None
                EID=None

            m1=manager() 
            m1.name=input("enter name :") 
            m1.age=int(input("enter age :"))
            m1.salary=int(input("enter salary :"))
            m1.department=input("enter department :")
            m1.EID=int(input("enter EID :"))

            print(f" Manager created with name = {m1.name} age = {m1.age} salary = {m1.salary} department = {m1.department} EiD = {m1.EID}")

            print("--choose another option--")


        case "4":
            
             



            




                
    
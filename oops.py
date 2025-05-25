class person:
    def __init__( self ,name , age):
        self.name = name
        self.age = age
    def display(self):
        print(f"name = {self.name} age = {self.age}")


class Employee(person):
    def __init__(self, name, emp_id, salary):
        self.__name = name
        self.__emp_id = emp_id
        self.__salary = salary

    
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_emp_id(self):
        return self.__emp_id

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        self.__salary = salary

 
    def display_info(self):
        print(f"Name: {self.__name}")
        print(f"Employee ID: {self.__emp_id}")
        print(f"Salary: ${self.__salary}")

    def update_info(self, name=None, salary=None):
        if name:
            self.set_name(name)
        if salary:
            self.set_salary(salary)


class Developer(Employee):
    def __init__(self, name, emp_id, salary, programming_language):
        super().__init__(name, emp_id, salary)
        self.programming_language = programming_language

    def display_info(self):
        super().display_info()
        print(f"Role: Developer")
        print(f"Programming Language: {self.programming_language}")


class Manager(Employee):
    def __init__(self, name, emp_id, salary, department ):
        super().__init__(name, emp_id, salary,department)
       

    def display_info(self):
        super().display_info()
        print(f"Role: Manager")
        print(f"Team Size: {self.team_size}")


people = []

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
            name =input("enter the name :")   
            age =input("enter the age :")
            p=person(name, age)
            people.append(p)
            print("person created successfully")

        case "2":
            name=input("enter the name:")
            age=input("enter the age: ")
            emp_id=int(input("enter the ID :"))
            salary=int(input("enter the salary"))
            e=Employee(name,age,salary,emp_id)
            people.append(e)
            print("employee created successfully")
        
        case "3":
            name=input("enter the name:")
            emp_id=int(input("enter the ID :"))
            salary=int(input("enter the salary :"))
            department=input("enter deparment :")
            m=Manager(name,department,salary,emp_id)
            people.append(m)
            print("manager  created successfully")

        case '4':

            while True:
                print("1. person")
                print("2. employee")
                print("3. manager")
                print("4. exit")

                choice2 = input("enter choice: ")

                match choice2:
                    case '1':
                        print("person details ")
                        print("-"*40)
                        for p in people:
                            if isinstance(p,person) and not isinstance(p,Employee):
                                p.display()
                                print("-"*40)

                    case '2':
                        print("employee details")
                        print("-"*40)
                        for person in people:
                            if isinstance(person,Employee) and not isinstance(person,(Manager)):
                                person.display()
                                print("-"*40)

                    case '3':
                        print("Manager details")
                        print("-"*40)
                        for person in people:
                            if isinstance(person,Manager):
                                person.display()
                                print("-"*40)
                    case '4':
                        print("Exiting...")
                        break

                    case __:
                        print("invalid option")
        case '5':



            emp_id1 = input("Enter the first employee's ID: ")
            emp_id2 = input("Enter the Secound Employee's ID: ")

            emp1 = None
            emp2 = None

            
            for p in people:
                if isinstance(p, Employee):
                    if p.get_emp_id() == emp_id1:
                        emp1 = p
                    if p.get_emp_id() == emp_id2:
                        emp2 = p

            if emp1 is None or emp2 is None:
                print("Enter valid ID number!! ")
            else:
                if emp1.get_salary() < emp2.get_salary():
                    print(f"Employee {emp1.name}{(emp_id1)} has lower salary than Manager {emp2.name} {(emp_id2)}")
                elif emp1.get_salary() == emp2.get_salary():
                    print("Dono ki salary barabar hai.")
                else:
                    print(f"{emp2.name} have more salary than {emp1.name} .")
  
                
                    
            

        case '6':
            print("Exiting the System. All Rsources have been freed")
            print("Good Bye!")
            break

        case ___:
            print("invalid choice , try again")
            

            











            



                

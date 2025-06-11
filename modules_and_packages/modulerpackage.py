import datetimemodule#import the datetime module
import mathmodule#import the math module
import randommodule#import the random module
import uuidmodule#import the uuid module
import filemodule#import the file module


print("="*60)
print("Welcome to multiutility toolkit")#welcome message


while True:
   
    print("="*60)#main menu
    print("choose an option (1-7):")
    print("1.Datetime and time operation")
    print("2.Mathematical operation")
    print("3.Random data generation")
    print("4.Generate unique identifiers")
    print("5.File operation(custome module)")
    print("6.Explore module attribute(dir())")
    print("7.Exit")
    print("="*60)

    choice = str(input("Enter your choice(1-7):"))

    match choice:
        case "1":
            while True:#datetime and time menu
                print("DateTime and Time Operation")
                print("1.Display current date and time")
                print("2.Calculate difference between two dated/times")
                print("3.Formate date into custom format")
                print("4.Stopwatch")
                print("5.Countdown Timer")
                print("6.Back to Main Menu")

                datetimechoice = str(input("Enter your choice (1-6):"))

                match datetimechoice:
                    case "1":
                        datetimemodule.currenrdatetime()              
                    case "2":
                        datetimemodule.difference_of_two_date()   
                    case "3":
                        datetimemodule.custom_date_format()  
                    case "4":
                        datetimemodule.simple_stopwatch()  
                    case "5":
                        datetimemodule.simple_countdown(10)
                    case "6":
                          break
        case "2":
            while True:#mathematical menu
                print("Mathematical Operation(1-5)")
                print("1.Calculate Factorial")
                print("2.Solve Compound Interest")
                print("3.Trigonometric Calculations")
                print("4.Area of Geometric Shapes")
                print("5.Back to Main Menu")

                mathematicalchoice = str(input("Enter your choice:"))

                match mathematicalchoice:
                    case "1":
                          mathmodule.calculate_fact()
                    case "2":
                          mathmodule.calculate_compoundrate()   
                    case "3":
                          mathmodule.trigonometric_calculation()  
                    case "4":
                          mathmodule.geometric_shape_calculator()  
                    case "5":
                          break
        case "3":
            while True:#random data menu
                print("Random Data Generation")
                print("1.Generate Random number")
                print("2.Generate Random list")
                print("3.Generate Random Password")
                print("4.Generate Random OTP")
                print("5.Back to Main Menu")

                randomchoice = str(input("Enter your choice(1-5):"))

                match randomchoice:
                    case "1":
                        randommodule.gerenerate_random_number()
                    case "2":
                        randommodule.generate_random_list()
                    case "3":
                        randommodule.generate_6_digit_password()
                    case "4":
                        randommodule.generate_otp()
                    case "5":
                        break
        case "4":
            while True:#uuid menu
                print("Generate Unique Identifiers")
                print("1.Generate UUID1(Based on timestamp and MAC address)")
                print("2.Generate UUID4(random UUID)")
                print("3.Back to Main Menu")

                uuidmodulechoice = str(input("Enter your choice(1-3):"))

                match uuidmodulechoice:
                    case "1":
                        uuidmodule.generate_uuid_base_timestamp()
                    case "2":
                        uuidmodule.generate_uuid4()
                    
                    case "3":
                        break

        case "5":
            while True:#file menu
                print("File Opeartion")
                print("1.Create a new file")
                print("2.write to a file")
                print("3.Read from a file")
                print("4.Append to a file")
                print("5.Back to Main Menu")

                filechoice = str(input("Enter your choice(1-5):"))

                match filechoice:
                    case "1":
                        filemodule.create_new_file()
                    case "2":
                        filemodule.write_to_file()
                    case "3":
                        filemodule.read_to_file()
                    case "4":
                        filemodule.append_to_file()
                    case "5":
                        break


        case "6":#dir() with module attribute
            print("Explore Module Attribute")
            module_name = input("Enter the module name to explore(e.g.,datetimemodule,mathmodule) ")  
            try:
                module = globals()[module_name]
                print(f"Available Attribute in {module_name} module")
                print("="*60)
                for attr in dir(module):
                    print(attr)
                print("="*60)    
            except KeyError:
                print(f"module {module_name} is not exit")


        case "7":
            print("="*60)
            print("Thank You for using the Multi-Utility Toolkit!")    
            print("="*60)

        case _:
            print("Please enter valis input from main menu...")    

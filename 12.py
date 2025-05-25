print("welcome to  pattern generator and number analyzer")

while True:

    print("generate a pattern")
    print("\n number analyzer")
    print("\n exit")

    choice=input("enter your choice :-")

    match choice:

        case "1":

            print("1, right angled trianngle")
            print("2, pyramid")
            print("3, left angled triangle")

            pattern_choice=("select the pattern :-")

            rows=int(input("\n enter no. of rows:- "))


            match pattern_choice:


                case "1":

                    print("-"*40)
                    print("pattern")
                    for i in range(1,rows+1):
                        print("*" * 1)
                    print("-"*40)

                case "2":

                    print("-"*40)
                    print("pattern")
                    for i in range(1,rows +1):
                        space = rows - i
                    print("-"*40)
                    star= 2*i-1
                    print("-"*40)

                case "3":

                    print("-"*40)
                    print("pattern")
                    for i in range(1,row +1):
                      spaces = ' ' * (1,row - i - 1)
                      stars = '*' * (2 * i + 1)
                      print(spaces + stars + spaces)
                    print("-"*40)
         

        case "2":

          start_range = int(input("\nenter stating range :- "))
          end_range = int(input("\nenter ending range :-"))
          sum = 0
          for i in range(start_range,end_range+1):
            if (i%2 == 0):
                 print(f"number is{i} even")
            else:
                 print(f"number is{i} odd")
                 sum=sum+i
                    
          print("\nsum of all no. is ",sum)

        case "3":

            print("exit")
            break
        case __:
            print("invalid")            
                
              

                  
         









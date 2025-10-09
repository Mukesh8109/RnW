import numpy as np  

class DataAnalytics:  

    def __init__(self):  
        self.array = None
        self.array2 = None

    def create1darr(self):  
        try:
            elements = input("Enter the elements for 1D Array separated by space: ")
            self.array = np.array(list(map(int, elements.split())))
            print(self.array)
            print("1D Array Created")
            print("=" * 40)
        except ValueError:
           print("Please enter valid integer elements.")
        except Exception as e:
           print("An unexpected error occurred:", e)



    def create2darr(self): 
        try:  
            row = int(input("Enter the number of Rows: "))  
            column = int(input("Enter the number of Columns: "))  
            print(f"Enter {row * column} elements separated by spaces:")
            elements = list(map(int, input().split()))  
            if len(elements) != row * column: 
                print("Incorrect number of elements. Please enter valid elements of given size.")
                return
            self.array = np.array(elements).reshape(row, column)
            print(self.array)
            print("2D Array Created")
            print("=" * 40)
        except ValueError:
            print("Please enter valid integers for rows, columns, and elements.")
        except Exception as e:
            print("An unexpected error occurred:", e)


    def create3darr(self): 
        try: 
            d = int(input("Enter depth for 3D array: "))  
            r = int(input("Enter number of Rows: "))
            c = int(input("Enter number of Columns: ")) 
            print(f"Enter {d * r * c} elements separated by space:")
            elements = list(map(int, input().split()))  
            if len(elements) != d * r * c:
                print("Incorrect number of elements.")
                return
            self.array = np.array(elements).reshape(d, r, c)
            print("3D Array Created:")
            print(self.array)
            print("=" * 40)
        except ValueError:
            print("Please enter valid integers for depth, rows, columns, and elements.")
        except Exception as e:
            print("An unexpected error occurred:", e)

    def addition1darr(self):  
        try:
            if self.array is None:
                print("Please create a 1D array first.")
                return
            print("Enter same number of elements for second 1D array:")
            elements = list(map(int, input().split()))
            if len(elements) != len(self.array):  
                print("Element count mismatch. Please try again.")
                return
            self.array2 = np.array(elements)
            print("\nOriginal Array:\n", self.array)
            print("\nSecond Array:\n", self.array2)
            add = np.add(self.array, self.array2)
            print("\nAddition Result:\n", add)
            print("=" * 40)
        except ValueError:
            print("Please enter valid integers for depth, rows, columns, and elements.")
        except Exception as e:
            print("An unexpected error occurred:", e)


    def subtraction1darr(self):  
        try:  
            if self.array is None:
                print("Please create a 1D array first.")
                return
            print("Enter same number of elements for second 1D array:")
            elements = list(map(int, input().split()))
            if len(elements) != len(self.array):
                print("Element count mismatch. Please try again.")
                return
            self.array2 = np.array(elements)
            print("\nOriginal Array:\n", self.array)
            print("\nSecond Array:\n", self.array2)
            sub = np.subtract(self.array, self.array2)
            print("\nSubtraction Result:\n", sub)
            print("=" * 40)
        except ValueError:
            print("Please enter valid integers for depth, rows, columns, and elements.")
        except Exception as e:
            print("An unexpected error occurred:", e)


    def division1darr(self):  
        try:
            if self.array is None:
                print("Please create a 1D array first.")
                return
            print("Enter same number of elements for second 1D array:")
            elements = list(map(int, input().split()))
            if len(elements) != len(self.array):
                print("Element count mismatch. Please try again.")
                return
            self.array2 = np.array(elements)
            print("\nOriginal Array:\n", self.array)
            print("\nSecond Array:\n", self.array2)
            div = np.divide(self.array, self.array2)
            print("\nDivision Result:\n", div)
            print("=" * 40)
        except ValueError:
            print("Please enter valid integers for depth, rows, columns, and elements.")
        except Exception as e:
            print("An unexpected error occurred:", e)



    def multiply1darr(self): 
        try:
            if self.array is None:
                print("Please create a 1D array first.")
                return
            print("Enter same number of elements for second 1D array:")
            elements = list(map(int, input().split()))
            if len(elements) != len(self.array):
                print("Element count mismatch. Please try again.")
                return
            self.array2 = np.array(elements)
            print("\nOriginal Array:\n", self.array)
            print("\nSecond Array:\n", self.array2)
            mul = np.multiply(self.array, self.array2)
            print("\nMultiplication Result:\n", mul)
            print("=" * 40)
        except ValueError:
            print("Please enter valid integers for depth, rows, columns, and elements.")
        except Exception as e:
            print("An unexpected error occurred:", e)


    def additsion2darr(self): 
        try:
            if self.array is None:
                print("Please create a 2D array first.")
                return
            row, column = self.array.shape
            print(f"Enter {row * column} elements separated by spaces for another array:")
            elements = list(map(int, input().split()))
            if len(elements) != row * column:
                print("Incorrect number of elements.")
                return
            self.array2 = np.array(elements).reshape(row, column)
            print("\nOriginal array\n", self.array)
            print("\nSecond array\n", self.array2)
            add = np.add(self.array, self.array2)
            print("=" * 40)
            print("Addition of array")
            print("=" * 40)
            print(add)
            print("=" * 40)
        except ValueError:
            print("Please enter valid integers for depth, rows, columns, and elements.")
        except Exception as e:
            print("An unexpected error occurred:", e)



    def subtraction2darr(self): 
        try:
            if self.array is None:
                print("Please create a 2D array first.")
                return
            row, column = self.array.shape
            print(f"Enter {row * column} elements separated by spaces for another array:")
            elements = list(map(int, input().split()))
            if len(elements) != row * column:
                print("Incorrect number of elements. Please enter valid elements.")
                return
            self.array2 = np.array(elements).reshape(row, column)
            print("\nOriginal array\n", self.array)
            print("\nSecond array\n", self.array2)
            sub = np.subtract(self.array, self.array2)
            print("=" * 40)
            print("Subtraction of array")
            print("=" * 40)
            print(sub)
            print("=" * 40)
        except ValueError:
            print("Please enter valid integers for depth, rows, columns, and elements.")
        except Exception as e:
            print("An unexpected error occurred:", e)


    def division2darr(self): 
        try:
            if self.array is None:
                print("Please create a 2D array first.")
                return
            row, column = self.array.shape
            print(f"Enter {row * column} elements separated by spaces for another array:")
            elements = list(map(int, input().split()))
            if len(elements) != row * column:
                print("Incorrect number of elements. Please enter valid elements.")
                return
            self.array2 = np.array(elements).reshape(row, column)
            print("\nOriginal array\n", self.array)
            print("\nSecond array\n", self.array2)
            div = np.divide(self.array, self.array2)
            print("=" * 40)
            print("Division of array")
            print("=" * 40)
            print(div)
            print("=" * 40)
        except ValueError:
            print("Please enter valid integers for depth, rows, columns, and elements.")
        except Exception as e:
            print("An unexpected error occurred:", e)

    def multiply2darr(self):
        try:
            if self.array is None:
                print("Please create a 2D array first.")
                return
            row, column = self.array.shape
            print(f"Enter {row * column} elements separated by spaces for another array:")
            elements = list(map(int, input().split()))
            if len(elements) != row * column:
                print("Incorrect number of elements. Please enter valid elements.")
                return
            self.array2 = np.array(elements).reshape(row, column)
            print("\nOriginal array\n", self.array)
            print("\nSecond array\n", self.array2)
            mul = np.multiply(self.array, self.array2)
            print("=" * 40)
            print("Multiplication of array")
            print("=" * 40)
            print(mul)
            print("=" * 40)
        except ValueError:
            print("Please enter valid integers for depth, rows, columns, and elements.")
        except Exception as e:
            print("An unexpected error occurred:", e)

    def combine2darrvertical(self):  
        try:
            if self.array is None:
                print("Please create a 2D array first.")
                return
            row, column = self.array.shape
            print(f"Enter {row * column} elements separated by spaces for another array:")
            elements = list(map(int, input().split()))
            if len(elements) != row * column:
                print("Incorrect number of elements. Please enter valid elements.")
                return
            self.array2 = np.array(elements).reshape(row, column)
            print("\nOriginal array\n", self.array)
            print("\nSecond array\n", self.array2)
            verticalstack = np.vstack((self.array, self.array2))
            print("=" * 40)
            print("Combined Array(Vertical stack):")
            print("=" * 40)
            print(verticalstack)
            print("=" * 40)
        except ValueError:
            print("Please enter valid integers for depth, rows, columns, and elements.")
        except Exception as e:
            print("An unexpected error occurred:", e)

    def combine2darrhorizontal(self): 
        try:
            if self.array is None:
                print("Please create a 2D array first.")
                return
            row, column = self.array.shape
            print(f"Enter {row * column} elements separated by spaces for another array:")
            elements = list(map(int, input().split()))
            if len(elements) != row * column:
                 print("Incorrect number of elements. Please enter valid elements.")
                 return
            self.array2 = np.array(elements).reshape(row, column)
            print("\nOriginal array\n", self.array)
            print("\nSecond array\n", self.array2)
            horizontalstack = np.hstack((self.array, self.array2))
            print("=" * 40)
            print("Combined Array(Horizontal stack):")
            print("=" * 40)
            print(horizontalstack)
            print("=" * 40)
        except ValueError:
            print("Please enter valid integers for depth, rows, columns, and elements.")
        except Exception as e:
            print("An unexpected error occurred:", e)


    def split_2d_array_vertical(self): 
        try:
            if self.array is None:
                 print("Please provide a 2D array first.")
                 return

            print("\nOriginal array\n", self.array)
    
            split_array = np.vsplit(self.array, 2)
            print("=" * 40)
            print("Split Array (Vertical):")
            print("=" * 40)
            i = 1
            for arr in split_array:
                print("Part", i)
                print(arr)
                i += 1
            print("=" * 40)
        except:
             print("please enter the elements")

    def split_2d_array_horizontal(self): 
        try:
            if self.array is None:
                print("Please provide a 2D array first.")
                return

            print("\nOriginal array\n", self.array)
            split_array = np.hsplit(self.array, 2)
            print("=" * 40)
            print("Split Array (Horizontal):")
            print("=" * 40)
            i = 1
            for arr in split_array:
                print("Part", i)
                print(arr)
                i += 1
            print("=" * 40)
        except:
            print("please enter the elements")
    
    def search2darrayvalue(self): 
        try:
            if self.array is None:
                print("Please create a 2D array first.")
                return
        
            value = int(input("Enter value to search: "))
            result = self.array[self.array == value]
            if result.size == 0:
                print("Value not found.")
            else:
                print("Value found :",result)
            print("=" * 40)
        except:
          print("please enter the elements")    
         

    def sort2darrayrow(self): 
        try:
            if self.array is None:
                print("Please create a 2D array first.")
                return
       
            rowwisesort = np.sort(self.array,axis=1)
            print("\nOriginal array\n", self.array)
            print("=" * 40)
            print("Sort Array(Row wise):")
            print("=" * 40)
            print(rowwisesort)
            print("=" * 40)
        except:
          print("please enter the elements")
    
    def sort2darraycolumn(self): 
        try:
            if self.array is None:
                print("Please create a 2D array first.")
                return
       
            columnwisesort = np.sort(self.array,axis=0)
            print("\nOriginal array\n", self.array)
            print("=" * 40)
            print("Sort Array(Column wise):")
            print("=" * 40)
            print(columnwisesort)   
            print("=" * 40)
        except:
            print("please enter the elements")

    def filtergreatervalues(self): 
        try: 
            if self.array is None:
                print("Please create a 2D array first.")
                return

            value = int(input("Enter the value: "))
            gtvalues = self.array[self.array > value]

            print("\nOriginal array\n", self.array)
            print("=" * 40)
            print(f"Filtered Array (Greater than {value}):")
            print("=" * 40)
            if gtvalues.size > 0:
                print(gtvalues.tolist())  
            else:
                print("No values greater than the given input.")
            print("=" * 40)
        except:
            print("please enter the elements")
    

    def filterlessvalues(self): 
        try:
            if self.array is None:
                print("Please create a 2D array first.")
                return

            value = int(input("Enter the value: "))
            ltvalues = self.array[self.array < value]

            print("\nOriginal array\n", self.array)
            print("=" * 40)
            print(f"Filtered Array (Less than {value}):")
            print("=" * 40)
            if ltvalues.size > 0:
                print(ltvalues.tolist()) 
            else:
                print("No values less than the given input.")
            print("=" * 40)
        except:
             print("please enter the elements")


    def filterequalvalues(self): 
        try:
            if self.array is None:
                print("Please create a 2D array first.")
                return

            value = int(input("Enter the value: "))
            eqvalues = self.array[self.array == value]

            print("\nOriginal array\n", self.array)
            print("=" * 40)
            print(f"Filtered Array (Equal to {value}):")
            print("=" * 40)
            if eqvalues.size > 0:
                print(eqvalues.tolist()) 
            else:
                print("No values less than the given input.")     
            print("=" * 40)
        except:
            print("please enter the elements")   

    def sumof2darray(self): # sum one 2D array
        try: 
            if self.array is None:
                print("Please create a 2D array first.")
                return 
            print("\nOriginal array\n", self.array)
            sumof2arr = np.sum(self.array)
            print("=" * 40)
            print("Sum:")
            print("=" * 40)
            print(sumof2arr)   
            print("=" * 40) 
        except:
            print("please enter the elements")

    def meanof2darray(self):
        try: 
            if self.array is None:
                print("Please create a 2D array first.")
                return 
            print("\nOriginal array\n", self.array)
            meanof2arr = np.mean(self.array)
            print("=" * 40)
            print("Mean:")
            print("=" * 40)
            print(meanof2arr)   
            print("=" * 40) 
        except:
             print("please enter the elements")

    def medianof2darray(self): 
        try:
            if self.array is None:
                print("Please create a 2D array first.")
                return 
            print("\nOriginal array\n", self.array)
            medianof2arr = np.median(self.array)
            print("=" * 40)
            print("Median:")
            print("=" * 40)
            print(medianof2arr)   
            print("=" * 40)
        except:
            print("please enter the elements")

    def stdof2darray(self): 
        try:
            if self.array is None:
                print("Please create a 2D array first.")
                return 
            print("\nOriginal array\n", self.array)
            stdof2arr = np.std(self.array)
            print("=" * 40)
            print("Standard Deviation:")
            print("=" * 40)
            print(stdof2arr)   
            print("=" * 40)    
        except:
            print("please enter the elements")

    def varianceof2darray(self): 
        try: 
            if self.array is None:
                print("Please create a 2D array first.")
                return 
            print("\nOriginal array\n", self.array)
            varof2arr = np.var(self.array)
            print("=" * 40)
            print("Variance:")
            print("=" * 40)
            print(varof2arr)   
            print("=" * 40)    
        except:
            print("please enter the elements")

    
    def index2darray(self):
        try: 
            if self.array is None:
              print("Please create a 2D array first.")
              return 
            rowindex = int(input("Enter the row for indexing:"))
            columnindex = int(input("Enter the column for indexing:"))
            
            indexing2d = self.array[rowindex,columnindex]
            print("\nOriginal array\n", self.array)
            print("=" * 40)
            print("Indexing:")
            print("=" * 40)
            print(indexing2d)   
            print("=" * 40)    
        except:
            print("please enter the elements")


    def slicingrdarray(self):
        try: 
            if self.array is None:
              print("Please create a 2D array first.")
              return 
            rowrange = input("Enter the row range (start:end): ")
            colrange = input("Enter the column range (start:end): ")

            row_start, row_end = map(int, rowrange.split(":"))
            col_start, col_end = map(int, colrange.split(":"))

            slicing2d = self.array[row_start:row_end, col_start:col_end]
            print("\nOriginal array\n", self.array)
            print("=" * 40)
            print("Slicing:")
            print("=" * 40)
            print(slicing2d)   
            print("=" * 40)    
        except:
            print("please enter the elements")

#
print("Welcome to Numpy Analyzer!")
print("="*50)
analytics = DataAnalytics()

while True:
    print("\nChoose an option:")
    print("1. Create Numpy array")
    print("2. Perform Mathematical Operation")
    print("3. Combine and Split Arrays")
    print("4. Search, Filter and Sort Array")
    print("5. Compute Aggregates and Statistics")
    print("6. Indexing,slicing")
    print("7. Exit")

    choice = input("Enter your choice : ")

    match choice:
        case "1":
            while True:
                print("\nSelect Array Type :")
                print("1. 1D Array")
                print("2. 2D Array")
                print("3. 3D Array")
                print("4. Back to Main Menu")

                arraychoice = input("Select the type of array to create: ")

                match arraychoice:
                    case "1":
                        analytics.create1darr()
                    case "2":
                        analytics.create2darr()
                    case "3":
                        analytics.create3darr()
                    case "4":
                        break
                    case _:
                        print("Invalid input. Please choose between ")

        case "2":
            while True:
                print("\nChoose Mathematical Operation:")
                print("1. Addition")
                print("2. Subtraction")
                print("3. Division")
                print("4. Multiplication")
                print("5. Back to Main Menu")

                mathschoice = input("Enter your choice : ")

                match mathschoice:
                    case "1":
                        print("\nSelect Array Type:")
                        print("1. 1D Array")
                        print("2. 2D Array")
                        print("3. Back")

                        subchoice = input("Enter choice: ")
                        match subchoice:
                            case "1":
                                analytics.addition1darr()
                            case "2":
                                analytics.additsion2darr()
                            case "3":
                                break
                            case _:
                                print("Invalid choice.")
                    case "2":
                        print("\nSelect Array Type:")
                        print("1. 1D Array")
                        print("2. 2D Array")
                        print("3. Back")

                        subchoice1 = input("Enter choice: ")
                        match subchoice1:
                            case "1":
                                analytics.subtraction1darr()
                            case "2":
                                analytics.subtraction2darr()
                            case "3":
                                break
                            case _:
                                print("Invalid choice.")
                    case "3":
                        print("\nSelect Array Type:")
                        print("1. 1D Array")
                        print("2. 2D Array")
                        print("3. Back")

                        subchoice3 = input("Enter choice: ")
                        match subchoice3:
                            case "1":
                                analytics.division1darr()
                            case "2":
                                analytics.division2darr()
                            case "3":
                                break
                            case _:
                                print("Invalid choice.")
                    case "4":
                        print("\nSelect Array Type:")
                        print("1. 1D Array")
                        print("2. 2D Array")
                        print("3. Back")

                        subchoice4 = input("Enter choice: ")
                        match subchoice4:
                            case "1":
                                analytics.multiply1darr()
                            case "2":
                                analytics.multiply2darr()
                            case "3":
                                break
                            case _:
                                print("Invalid choice.")
                    
                    case "5":
                        break

                    case _:
                       print("Please enter a valid option from the list.")


        case "3":
            while True:
                print("Choose an option")
                print("1.Combine Arrays")
                print("2.Split Array")
                print("3.Back Menu")

                combinesplitchoice = input("Enter your choice:")

                match combinesplitchoice:
                    case "1":
                         while True:
                            print("Choose an option")
                            print("1.Combine Arrays vertically(By Rows)")
                            print("2.Combine Array Horizontally(By Colums)")
                            print("3.Back Menu")

                            combinechoice = input("Enter your choice(1-3):")

                            match combinechoice:
                                case "1":
                                   analytics.combine2darrvertical()
                                case "2":
                                   analytics.combine2darrhorizontal()
                                case "3":
                                   break
                                
                    case "2":
                       while True:
                            print("Choose an option")
                            print("1.Split Arrays vertically(By Rows)")
                            print("2.Split Array Horizontally(By Colums)")
                            print("3.Back Menu")

                            splitchoice = input("Enter your choice:")

                            match splitchoice:
                                case "1":
                                   analytics.split_2d_array_vertical()
                                case "2":
                                   analytics.split_2d_array_horizontal()
                                case "3":
                                   break
                                
                    case "3":
                        break
                      
        case "4":
            while True:
                print("Choose an option:")
                print("1.search the value")
                print("2.Sort the array")
                print("3.Filter the value")
                print("4.Back Menu")

                searchfiltersortchoice = input("Enter your choice:")

                match searchfiltersortchoice:
                    case "1":
                        analytics.search2darrayvalue()
                    case "2":
                        while True:
                           print("Select an option:")
                           print("1.Sort the array(Row wise)")
                           print("2.Sort the array(Column wise)")
                           print("3.Back Menu")
                           searchchoice = input("Enter your choice:")
                           match searchchoice:
                                case "1":
                                   analytics.sort2darrayrow()
                                case "2":
                                   analytics.sort2darraycolumn()
                                case "3":
                                   break
                    case "3":
                        while True:
                           print("Select an option:")
                           print("1.Filter the array(Greter value)")
                           print("2.Filter the array(Less value)")
                           print("3.Filter the array(Equal value)")
                           print("4.Back Menu")

                           filterchoice = input("Enter your choice:")
                           match filterchoice:
                                case "1":
                                   analytics.filtergreatervalues()
                                case "2":
                                   analytics.filterlessvalues()
                                case "3":
                                   analytics.filterequalvalues()
                                case "4":
                                   break         
                    case "4":
                        break           

        case "5":
            while True:
                print("Select an Option:")
                print("1.Sum")
                print("2.Mean")
                print("3.Median")
                print("4.Standard Deviation")
                print("5.Variance")
                print("6.Back Menu")

                aggregatestatechoice = input("Enter your choice:")

                match aggregatestatechoice:
                    case "1":
                        analytics.sumof2darray()
                    case "2":
                        analytics.meanof2darray()
                    case "3":
                        analytics.medianof2darray()
                    case "4":
                        analytics.stdof2darray()
                    case "5":
                        analytics.varianceof2darray()
                    case "6":
                        break
        case "6":
            while True:
                print("Select an option:")
                print("1.indexing")
                print("2.Slicing")
                print("3.Back Menu")

                indexslicingchoice = input("Enter your choice:")

                match indexslicingchoice:
                    case "1":
                        analytics.index2darray()
                    case "2":
                        analytics.slicingrdarray()
                    case "3":
                        break 

        case "7":
            print("Exiting... Thank you!")
            break
        case _:
            print("Please enter a valid option from the list.")

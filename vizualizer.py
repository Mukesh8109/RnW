# import numpy as np
# import matplotlib.pyplot as plt
# from datetime import datetime, timedelta
# import pandas as pd
# import seaborn as sns

# class salesAnalyzer:
    
#         def __init__(self):
#             self.data = None

#         def load_dataset(self):
#             print("====load dataset===")
#             filepath=input("enter the path of dataset (CSV):")
#             try:
#                 self.data=pd.read_csv()
#                 print("dataset loaded successfully")
#                 print(self.data)
#             except FileNotFoundError:
#                 print("File not found. Please check the path and try again.")
#             except Exception as e:
#                 print(f"An error occurred: {e}")
#             print("="*30)

            

#         def display_5_rows(self):
#             try:
#                 print("display first 5 rows")
#                 fiverows=self.data.head()
#                 print(fiverows)
#             except Exception as e:
#                print(f"An error occurred: {e}")
#             print("="*30)

#         def display_last_5rows(self):
#             try:
#                 print("display last 5 rows ")
#                 last5rows=self.data.tail() 
#                 print(last5rows)
#             except Exception as e:
#                print(f"An error occurred: {e}")
#             print("="*30)

#         def display_col_names(self):
#             try:
#                 print("display column names")
#                 columnname = self.data.columns.tolist()
#                 print(columnname)
#             except Exception as e:
#                print(f"An error occurred: {e}")
#             print("="*30)
            

#         def display_datatypes(self):
#             try:
#                 print("datatypes")
#                 datatype=self.data.dtypes()
#                 print(datatype)
#             except Exception as e:
#                print(f"An error occurred: {e}")
#             print("="*30)

#         def display_info(self):
#             try:
#                 print(" display basic info")
#                 info=self.data.info()
#                 print(info)
#             except Exception as e:
#                print(f"An error occurred: {e}")
#             print("="*30)

#         def rowwithmissvalue(self):
#             try:
#                 print("\nRows with missing values:\n")
#                 missing_rows = self.data[self.data.isnull().any(axis=1)]
#                 if missing_rows.empty:
#                     print("No missing values found.")
#                 else:
#                     print(missing_rows)
#                     print(f"\nTotal rows with missing values: {len(missing_rows)}")
#             except Exception as e:
#                     print(f"An error occurred: {e}")
#             print("=" * 40)
        
#         def fillwithmean(self):
#             try:
#                    print("\nFilling missing values with column mean...\n")
#                    before_missing = self.data.isnull().sum()
#                    self.data.fillna(self.data.mean(numeric_only=True), inplace=True)
#                    after_missing = self.data.isnull().sum()

#                    print("Missing values filled with mean successfully.")
#                    print("\nMissing values before fill:\n", before_missing)
#                    print("\nMissing values after fill:\n", after_missing)
#                    print("\nSample data after fill:\n", self.data.head())
#             except Exception as e:
#                    print(f"An error occurred: {e}")
#             print("=" * 40)

#         def droprowwithmissvalue(self):
#             try:
#                 print("\nDropping rows with missing values...\n")
#                 before = len(self.data)
#                 self.data.dropna(inplace=True)
#                 after = len(self.data)
#                 dropped = before - after

#                 print(f"Dropped {dropped} row(s) containing missing values.")
#                 print("\nSample data after drop:\n", self.data.head())
#             except Exception as e:
#                     print(f"An error occurred: {e}")
#             print("=" * 40)

#         def replacewithmissvalue(self):
#                 print("\nReplace missing values with a specific value\n")
#                 value = input("Enter the value to fill missing values: ")

#                 try:
#                      # Try to convert to float for numeric fill
#                     value = float(value)
#                 except ValueError:
#                     pass  # Keep as string if not convertible

#                 try:
#                    before_missing = self.data.isnull().sum()
#                    self.data.fillna(value, inplace=True)
#                    after_missing = self.data.isnull().sum()

#                    print("Missing values replaced successfully.")
#                    print("\nMissing values before replace:\n", before_missing)
#                    print("\nMissing values after replace:\n", after_missing)
#                    print("\nSample data after replace:\n", self.data.head())
#                 except Exception as e:
#                    print(f"An error occurred: {e}")
#                 print("=" * 40)

#         def search_similar(self):
#             try:
#                 column = input("Enter the column to search in (e.g., product, region): ").strip()
#                 if column not in self.data.columns:
#                     print("Invalid column name.")
#                     return

#                 keyword = input("Enter the search keyword: ").strip().lower()
#                 results = self.data[self.data[column].str.lower().str.contains(keyword)]

#                 if not results.empty:
#                     print(f"\nSearch results for '{keyword}' in '{column}':")
#                     print(results)
#                 else:
#                     print("No matching records found.")
#             except Exception as e:
#                 print(f"An error occurred: {e}")
#             print("=" * 30)


#         def statistics_analysis(self):
#             try:
#                print("\nStatistics Analysis :\n")

#                statisaticsinfo = self.data.describe()
#                print(statisaticsinfo)
            
#             except Exception as e:
#                print(f"An error occurred: {e}")
#             print("="*30)

#         def combine_data(self):
#             try:
#                 print("\nCombine Dataframe:\n")
#                 m = pd.read_csv("movies.csv")
#                 m.columns = ['col1', 'col2', 'col3', 'col4', 'col5']
#                 self.data.columns = ['col1', 'col2', 'col3', 'col4', 'col5']
#                 combinedata = pd.concat([self.data,m])
#                 print(combinedata)
#                 print("=" * 30)

#                 return combinedata
#             except Exception as e:
#                 print(f"An error occurred: {e}")
#                 return None
            

#         def spilt_data(self,combinedata):
#             try:
#                 movie_df = pd.read_csv("movies.csv")
#                 movie_len = len(movie_df)

#                 sales_split = combinedata.iloc[:-movie_len].reset_index(drop=True)
#                 movie_split = combinedata.iloc[-movie_len:].reset_index(drop=True)

#                 print("\nSales DataFrame:\n", sales_split)
#                 print("\nMovie DataFrame:\n", movie_split)

#                 return sales_split, movie_split

#             except Exception as e:
#                 print(f"An error occurred: {e}")


#         def addofsp(self):
#             try:
#                 print("\nSum:\n")
#                 salessum = self.data['sales'].sum()
#                 profitsum = self.data['profit'].sum()
#                 print(f"sales = {salessum}\t profit = {profitsum}")
#             except Exception as e:
#                 print(f"An error occurred: {e}")
#             print("=" * 30)


#         def meanofsp(self):
#             try:
#                 print("\nMean:\n")
#                 salesmean = self.data['sales'].mean()
#                 profitmean = self.data['profit'].mean()
#                 print(f"sales = {salesmean}\t profit = {profitmean}")
#             except Exception as e:
#                 print(f"An error occurred: {e}")
#             print("=" * 30)
        

#         def countofsp(self):
#             try:
#                 print("\nCount:\n")
#                 salescount = self.data['sales'].count()
#                 profitcount = self.data['profit'].count()
#                 print(f"sales = {salescount}\t profit = {profitcount}")
#             except Exception as e:
#                 print(f"An error occurred: {e}")
#             print("=" * 30)

#         def create_pivot_table(self):
#             try:
#                  print("\nCreate Pivot Table:\n")
#                  print("Available columns:")
#                  print(self.data.columns.tolist())

#                  index_col = input("Enter the column to use as index (e.g., 'region'): ").strip()
#                  columns_col = input("Enter the column to use as columns (e.g., 'product'): ").strip()
#                  values_col = input("Enter the column to aggregate (e.g., 'sales'): ").strip()
#                  agg_func = input("Enter aggregation function (sum, mean, count): ").strip().lower()

#                  if index_col not in self.data.columns or columns_col not in self.data.columns or values_col not in self.data.columns:
#                     print("One or more column names are invalid.")
#                     return

#                  if agg_func not in ["sum", "mean", "count"]:
#                    print("Invalid aggregation function. Choose from sum, mean, or count.")
#                    return

#                  pivot = pd.pivot_table(
#                      self.data,
#                      index=index_col,
#                      columns=columns_col,
#                      values=values_col,
#                      aggfunc=agg_func,
#                      fill_value=0
#                     )

#                  print("\nPivot Table:")
#                  print(pivot)

#             except Exception as e:
#                 print(f"An error occurred: {e}")
#             print("=" * 40)

#         def bar_plot(self):
#             try:
#                 print("\nBar Plot:\n")
#                 print("Available columns:", self.data.columns.tolist())
        
#                 x_col = input("Enter the column for X-axis (e.g., 'product', 'region'): ").strip()
#                 y_col = input("Enter the column for Y-axis (e.g., 'sales', 'profit'): ").strip()

#                 if x_col not in self.data.columns or y_col not in self.data.columns:
#                    print("Invalid column names provided.")
#                    return
                
#                 sns.set_style("darkgrid")
#                 plt.figure(figsize=(10, 6))
#                 sns.barplot(data=self.data, x=x_col, y=y_col,color='skyblue')
#                 plt.title(f"Bar Plot of {y_col} by {x_col}")
#                 plt.xlabel(x_col)
#                 plt.ylabel(y_col)
#                 plt.xticks(rotation=45)
#                 plt.tight_layout()
#                 plt.show()
#                 plt.savefig()
#             except Exception as e:
#                 print(f"An error occurred: {e}")
            
 
#         def line_plot(self):
#             try:
#                 print("\nLine Plot:\n")
#                 print("Available columns:", self.data.columns.tolist())

#                 x_col = input("Enter the column for X-axis (e.g, 'Date'): ").strip()
#                 y_col = input("Enter the column for Y-axis (e.g, 'sales','profit','product','region'): ").strip()

#                 if x_col not in self.data.columns or y_col not in self.data.columns:
#                     print("Invalid column names.")
#                     return
                
                
#                 self.data[x_col] = pd.to_datetime(self.data[x_col])
#                 self.data.sort_values(by=x_col, inplace=True)
                
#                  # Basic line plot
#                 sns.set_style("darkgrid")
#                 plt.figure(figsize=(10, 5))
#                 sns.lineplot(data=self.data, x=x_col, y=y_col,color='skyblue')
#                 plt.title(f'{y_col.capitalize()} vs {x_col.capitalize()}')
#                 plt.xticks(rotation=45)
#                 plt.tight_layout()
#                 plt.show()

#             except Exception as e:
#                 print(f"An error occurred: {e}")
           

#         def scatter_plot(self):
#             try:
#                 print("\nScatter Plot:\n")
#                 print("Available columns:", self.data.columns.tolist())

#                 x_col = input("Enter the column for X-axis (e.g, 'sales'): ").strip()
#                 y_col = input("Enter the column for Y-axis (e.g, 'profit'): ").strip()

#                 if x_col not in self.data.columns or y_col not in self.data.columns:
#                     print("Invalid column names.")
#                     return
#                # Basic scatter plot

#                 sns.set_style("darkgrid")
#                 plt.figure(figsize=(10, 5))
#                 sns.scatterplot(data=self.data, x=x_col, y=y_col,color='skyblue')
#                 plt.title(f'{y_col.capitalize()} vs {x_col.capitalize()}')
#                 plt.xticks(rotation=45)
#                 plt.tight_layout()
#                 plt.show()

#             except Exception as e:
#                 print(f"An error occurred: {e}")
           

#         def histo_gram(self):
#             try:
#                 print("\nHistogram:\n")
#                 print("Available columns:", self.data.columns.tolist())

#                 x_col = input("Enter the column for X-axis (e.g, 'sales','profit'): ").strip()

#                 if x_col not in self.data.columns: 
#                     print("Invalid column names.")
#                     return
#                # Basic histogram
#                 if not pd.api.types.is_numeric_dtype(self.data[x_col]):
#                     print(f"The column '{x_col}' is not numeric and cannot be used for a histogram.")
#                     return
                
#                 sns.set_style("darkgrid")
#                 plt.figure(figsize=(10, 5))
#                 sns.histplot(data=self.data, x=x_col,bins=24,color='skyblue')
#                 plt.title(f'{x_col.capitalize()}')
#                 plt.xticks(rotation=45)
#                 plt.tight_layout()
#                 plt.show()

#             except Exception as e:
#                 print(f"An error occurred: {e}")
           
#         def pie_chart(self):
#             try:
#                 print("\nPie Chart:\n")
#                 print("Available columns:", self.data.columns.tolist())

#                 label_col = input("Enter the column for labels (e.g., 'region', 'product'): ").strip()
#                 value_col = input("Enter the numeric column for values (e.g., 'sales', 'profit'): ").strip()

#                 if label_col not in self.data.columns or value_col not in self.data.columns:
#                     print("Invalid column names.")
#                     return

#                 # Aggregate values
#                 pie_data = self.data.groupby(label_col)[value_col].sum()

#                 sns.set_palette("pastel")  # Use Seaborn color palette
#                 plt.figure(figsize=(8, 8))
#                 plt.pie(pie_data, labels=pie_data.index, autopct='%1.1f%%', startangle=140)
#                 plt.title(f'{value_col.capitalize()} Distribution by {label_col.capitalize()}')
#                 plt.axis('equal')
#                 plt.tight_layout()
#                 plt.show()

#             except Exception as e:
#                 print(f"An error occurred: {e}")
           


#         def stack_chart(self):  
#             try:
#                 print("\nStack Plot:\n")
#                 print("Available columns:", self.data.columns.tolist())

#                 x_col = input("Enter the column for X-axis (should be categorical/time-based): ").strip()
#                 y_cols_input = input("Enter numeric columns for stacking (comma-separated, e.g., 'sales,profit'): ").strip()
#                 y_cols = [col.strip() for col in y_cols_input.split(",")]

#                 if x_col not in self.data.columns or any(col not in self.data.columns for col in y_cols):
#                     print("One or more column names are invalid.")
#                     return

#                 stacked_data = self.data.groupby(x_col)[y_cols].sum()

#                 sns.set_style("whitegrid")  # Apply Seaborn style
#                 plt.figure(figsize=(10, 6))
#                 plt.stackplot(stacked_data.index, stacked_data.T, labels=stacked_data.columns, alpha=0.8, colors=sns.color_palette("pastel"))
#                 plt.title(f'Stack Plot by {x_col}')
#                 plt.xlabel(x_col)
#                 plt.ylabel("Values")
#                 plt.legend(loc='upper left')
#                 plt.xticks(rotation=45)
#                 plt.tight_layout()
#                 plt.show()

#             except Exception as e:
#                 print(f"An error occurred: {e}")

#         def save_fig(self):
#             save = input("Do you want to save this file (Yes/No):")
#             if save == "Yes":
                
#                 filename = input("Enter the file name to save the plot (e.g.,bar_plot.png,line_plot.png):")
#                 try:
#                     plt.savefig(filename)
#                     print(f"Visulization is saved as {filename} successfully")    
#                 except Exception as e:
#                     print(f"An error occurred: {e}")

# sales = salesAnalyzer()

# print("================Data Analysis &  visulization Program==================")
# while True:
#     print("Select an option:")
#     print("1. Load Dataset")
#     print("2. Explore Data")
#     print("3. Perform Dataframe Operation")
#     print("4. Handle Missing Data")
#     print("5. Generate Discriptive Statistics")
#     print("6. Generate pivot table")
#     print("7. Data Visulization")
#     print("8. Save Visulization")
#     print("9. Exit")
#     print("="*50)

#     choice=input("enter your choice : ")

#     match choice:
#         case "1":
#             salesAnalyzer.load_dataset()
#         case "2":
#             print("===Explore Data===")
#             while True:
#                 print("Select an option:")
#                 print("1. Display the top 5 rows")
#                 print("2. Display the last 5 rows")
#                 print("3. Display column name")
#                 print("4. Display Datatype")
#                 print("5. Display the basic info")
#                 print("6. Back menu")

#                 datachoice=input("Select an option :")

#                 match datachoice:

#                     case "1":
#                         salesAnalyzer.display_5_rows()
#                     case "2":
#                         salesAnalyzer.display_last_5rows()
#                     case "3":
#                         salesAnalyzer.display_col_names()
#                     case "4":
#                         salesAnalyzer.display_datatypes()
#                     case "5":
#                         salesAnalyzer.display_info()
#                     case "6":
#                         break
#                     case _:
#                         print("Invalid input. Please choose between ")            

#         case "3":
#             print("===dataframe opeartions===")
#             while True:
                
#                 print("Select an option:")
#                 print("1.  Search")
#                 print("2. Aggregate Function(sum,mean,count)")
#                 print("3. Combine Data")
#                 print("4. Spilt Data")
#                 print("5. Back to Main Menu")
                

#                 maths1choice = input("Enter your choice: ")

#                 match maths1choice:
#                     case "1":
#                         salesAnalyzer.search_similar()
#                     case "2":
#                         print("===aggregate functions===")
#                         while True:
#                             print("select an option")
#                             print("1. Sum")
#                             print("2. Mean")
#                             print("3. Count")
#                             print("4. Back to Previous Menu")

#                             aggeregate_choice = input("Enter your choice:")
#                             match aggeregate_choice:
#                                 case "1":
#                                     sales.addofsp()
#                                 case "2":
#                                     sales.meanofsp()
#                                 case "3":
#                                     sales.countofsp()
#                                 case "4":
#                                     break
#                     case "3":
#                         salesAnalyzer.combine_data()
#                     case "4":
#                         salesAnalyzer.spilt_data()
#                     case "5":
#                         break

#         case "4":
#             print("===Handling missing data===")
#             while True:
#                 print("Select an option")
#                 print("1. Display rows with missing values")
#                 print("2. Fill missing values with mean")
#                 print("3. Drop rows with missing values")
#                 print("4. Replace missing values with a specific value")
#                 print("5. Back Menu")
                
#                 misschoice = input("Enter your choice:")

#                 match misschoice:
#                     case "1":
#                         sales.rowwithmissvalue()
#                     case "2":
#                         sales.fillwithmean()
#                     case "3":
#                         sales.droprowwithmissvalue()
#                     case "4":
#                         sales.replacewithmissvalue()
#                     case "5":
#                         break 
                    
                    

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class load_data():
    def _init_(self):
        self.df = None
        self.last_plot_saved = False

    def data(self):
        try:
            entry = input("Enter The Path of The DataSet (CSV File) ")
            self.df = pd.read_csv(entry)
            print("Data Successfully loaded")
        except FileNotFoundError:
            print("File not found please try again!")
            
    def explore_data(self):
        if self.df is None:
            print(" No Dataset loaded. please try again!!")
            return
        
        while True:
                print("\n")
                print("1. Display The First 5 rows")
                print("2. Display the Last 5 rows")
                print("3. Display Column names")
                print("4. Display Data types")
                print("5. Exit")
                print("\n")
                choice1 = input("Enter your Choice: ")
                match choice1:
                    case '1':
                        print(self.df.head(5))
                    case '2':
                        print(self.df.tail(5))
                    case '3':
                        print("Columns name: ",list(self.df.columns))
                    case '4':
                        print("Datatpes: ",self.df.dtypes)
                    case '5':
                        print("Exiting..")
                        break
                    case _:
                        print("Invalid option")

    def handle_missing_data(self):
        
        if self.df is None:
            print(" No Dataset loaded. please try again!!")
            return
        
        while True:
            print("1. Display rows with missing values")
            print("2. Fill missing values with mean")
            print("3. drop Rows With missing values")
            print("4. Replace missing values with a specific value")
            print("5. Exit")
            
            choice2 = input("ENter your choice: ")
            match choice2:
                case'1':
                    missing_rows = self.df[self.df.isnull().any(axis=1)]
                    print(missing_rows)
                case '2':
                    r = self.df.fillna(self.df.mean(numeric_only=True), inplace=True)
                    print("Filled numeric missing values with column means.")
                    print(r)
                case '3':
                    r = self.df.dropna()
                    print(" Dropped all rows with any missing values.")
                case '4':
                    d = self.df.columns
                    print(d)
                    col = input("Enter the column name to fill: ")
                    if col not in self.df.columns:
                        print(f" Column '{col}' not found.")
                        continue
                    val = input("Enter the value to replace missing values with: ")
                    try:
                    
                          val = float(val)
                    except ValueError:
                        pass 
                    self.df[col].fillna(val, inplace=True)
                    print(f"Missing values in column '{col}' replaced with '{val}'.")

                case '5':
                    
                    print("Exiting..")
                    break
                case _:
                 print("Invalid option")

    def descriptive_statistics(self):
        if self.df is None:
                        print("please load data")
                        return
        print(self.df.describe())

    
    def data_visulaization(self):
        while True:
             print('1. Bar Plot')
             print('2. Line Plot')
             print('3. Scatter Plot')
             print('4. Pie Chart')
             print('5. Histogram')
             print('6. Stack Plot')
             print("7 Heatmap")
             print('8. Exit')
             
             choice3 = input("Enter your choice: ")

             match choice3:
                  case '1':
                    print("\nAvailable columns:", list(self.df.columns))

                    xx = input("Enter x-axis column name: ")
                    yy = input("Enter y-axis column name: ")

                    try:
                        if xx not in self.df.columns or yy not in self.df.columns:
                            raise KeyError(f"One or both column names are invalid: '{xx}', '{yy}'")

                        self.df[yy] = pd.to_numeric(self.df[yy], errors='coerce') #avoid program to crash by converting to them into nan or string
                        plot_df = self.df[[xx, yy]].dropna() #drop missing values

                        if plot_df.empty:
                            print(" No valid data to plot after cleaning. Check for missing or non-numeric values.")
                        else:
                            plt.figure(figsize=(10, 6))
                            plt.bar(plot_df[xx], plot_df[yy], color='skyblue')
                            plt.xlabel(xx)
                            plt.ylabel(yy)
                            plt.title(f'{yy} by {xx}')
                            plt.xticks(rotation=45)
                            plt.tight_layout()
                            self.last_plot = plt  # after plotting
                            self.last_plot_saved = True

                            plt.show()

                            save = input("Do you want to save this plot? (yes/no): ").lower()
                            if save == "yes":
                                file_name = input("Enter the file name (with .png or .jpg): ")
                                try:
                                    plt.savefig(file_name)
                                    print(f"Plot saved as '{file_name}'")
                                except Exception as e:
                                    print("Error saving plot:", e)


                    except KeyError as e:
                        print(e)
                    except Exception as e:
                        print("An unexpected error occurred:", e)


                  case '2':
                     print("\nAvailable columns: ", list(self.df.columns))
                     xx = input("Enter x-axis column name: ")
                     yy = input("Enter y-axis column name: ")

                     try:
                         if xx not in self.df.columns or yy not in self.df.columns:
                             raise KeyError("One or both columns are not valid")
                         
                         self.df[yy] = pd.to_numeric(self.df[yy],errors='coerce')
                         self.df[xx] = pd.to_numeric(self.df[xx], errors='coerce')

                         plot_df = self.df[[xx,yy]].dropna()

                         if plot_df.empty:
                             print("No valid data to plot after cleaining")
                         else:
                             plt.figure(figsize=(10,6))
                             plt.plot(plot_df[xx],plot_df[yy],marker='o',color='green')
                             plt.xlabel(xx)
                             plt.ylabel(yy)
                             plt.title(f'{yy} over {xx}')
                             plt.grid(True)
                             plt.xticks(rotation=45)
                             plt.tight_layout()
                             self.last_plot = plt 
                             self.last_plot_saved = True
                             plt.show()
                             save = input("Do you want to save this plot? (yes/no): ").lower()
                             if save == "yes":
                                file_name = input("Enter the file name (with .png or .jpg): ")
                                try:
                                    plt.savefig(file_name)
                                    print(f"Plot saved as '{file_name}'")
                                except Exception as e:
                                    print("Error saving plot:", e)                             
                             
                     except KeyError as e:
                         print(e)
                     except Exception as e:
                         print("An unexpected error occured ",e)

                  case '3':
                    print("\nAvailable Columns: ",list(self.df.columns))
                    xx = input("Enter Column name: ")
                    yy = input("Enter 2nd Column name: ")
                    try:
                        if xx not in self.df.columns or yy not in self.df.columns:
                            raise KeyError("one or both columns are not valid")
                        self.df[xx] = pd.to_numeric(self.df[xx],errors='coerce')
                        self.df[yy] = pd.to_numeric(self.df[yy],errors='coerce')

                        plot_df = self.df[[xx, yy]].dropna()
                        if plot_df.empty:
                            print("No valid data to plot after cleaning. Check for non-numeric values or missing data.")
                        else:
                            plt.figure(figsize=(10, 6))
                            plt.scatter(plot_df[xx], plot_df[yy], color='purple', alpha=0.7)
                            plt.xlabel(xx)
                            plt.ylabel(yy)
                            plt.title(f'Scatter Plot: {yy} vs {xx}')
                            plt.grid(True)
                            plt.tight_layout()
                            self.last_plot = plt 
                            self.last_plot_saved = True
                            plt.show()

                            save = input("Do you want to save this plot? (yes/no): ").lower()
                            if save == "yes":
                                file_name = input("Enter the file name (with .png or .jpg): ")
                                try:
                                    plt.savefig(file_name)
                                    print(f"Plot saved as '{file_name}'")
                                except Exception as e:
                                    print("Error saving plot:", e)

                    except KeyError as e:
                            print(e)
                    except Exception as e:
                            print("An unexpected error occurred:", e)
                  case '4':
                    print("\nAvailable columns:", list(self.df.columns))

                    col = input("Enter the column to visualize as a pie chart: ")

                    if col not in self.df.columns:
                        print(f"Column '{col}' not found in dataset.")
                        continue

                    # Count values in the column
                    value_counts = self.df[col].value_counts().dropna()

                    if value_counts.empty:
                        print("No valid data to plot.")
                    else:
                        plt.figure(figsize=(8, 8))
                        plt.pie(value_counts, labels=value_counts.index, autopct='%1.1f%%', startangle=140)
                        plt.title(f'Distribution of {col}')
                        plt.axis('equal')  # keeps pie chart round
                        plt.tight_layout()
                        self.last_plot = plt 
                        self.last_plot_saved = True
                        plt.show()
                        save = input("Do you want to save this plot? (yes/no): ").lower()
                        if save == "yes":
                                file_name = input("Enter the file name (with .png or .jpg): ")
                                try:
                                    plt.savefig(file_name)
                                    print(f"Plot saved as '{file_name}'")
                                except Exception as e:
                                    print("error saving plot:", e)
                  case '5':
                    print("\nAvailable numeric columns:", self.df.select_dtypes(include='number').columns.tolist())
                    col = input("Enter the column to create histogram: ")

                    if col not in self.df.columns:
                        print(f"Column '{col}' not found.")
                        continue

                    try:
                        data = pd.to_numeric(self.df[col], errors='coerce').dropna()

                        if data.empty:
                            print("No valid numeric data to plot.")
                        else:
                            plt.figure(figsize=(10, 6))
                            counts, bins , patches = plt.hist(data, bins=10, color='skyblue', edgecolor='black')

                            bin_center = 0.5 * (bins[1:] + bins[:-1])
                            plt.xticks(bin_center.round(2))

                            plt.xlabel(col)
                            plt.ylabel("Frequency")
                            plt.title(f"Histogram of {col}")
                            plt.grid(axis='y')
                            plt.tight_layout()
                            self.last_plot = plt 
                            self.last_plot_saved = True
                            plt.show()
                            save = input("Do you want to save this plot? (yes/no): ").lower()
                            if save == "yes":
                                file_name = input("Enter the file name (with .png or .jpg): ")
                                try:
                                    plt.savefig(file_name)
                                    print(f"Plot saved as '{file_name}'")
                                except Exception as e:
                                    print("Error saving plot:", e)                            
                    except Exception as e:
                        print("Error creating histogram:", e)

                  case '6':

                    numeric_cols = self.df.select_dtypes(include='number').columns.tolist()
                    print("\nAvailable numeric columns:", numeric_cols)
                    
                    x_col = input("Enter x-axis column (base for stacking): ")

                    if x_col not in self.df.columns:
                        print(f"Column '{x_col}' not found.")
                        continue

                    y_cols = input("Enter y-axis columns to stack (comma-separated): ").split(',')

                    y_cols = [col.strip() for col in y_cols if col.strip() in self.df.columns]

                    if not y_cols:
                        print("No valid y-axis columns selected.")
                        continue

                    try:
                        stack_data = self.df[[x_col] + y_cols].dropna()

                        if stack_data.empty:
                            print("No valid data to plot after cleaning.")
                        else:
                            plt.figure(figsize=(10, 6))
                            plt.stackplot(stack_data[x_col], [stack_data[col] for col in y_cols], labels=y_cols)
                            plt.xlabel(x_col)
                            plt.ylabel("Value")
                            plt.title(f"Stack Plot of {', '.join(y_cols)} over {x_col}")
                            plt.legend(loc='upper left')
                            plt.tight_layout()
                            self.last_plot = plt 
                            self.last_plot_saved = True
                            plt.show()
                            save = input("Do you want to save this plot? (yes/no): ").lower()
                            if save == "yes":
                                file_name = input("Enter the file name (with .png or .jpg): ")
                                try:
                                    plt.savefig(file_name)
                                    print(f"Plot saved as '{file_name}'")
                                except Exception as e:
                                    print("Error saving plot:", e)                            
                    except Exception as e:
                        print("Error creating stack plot:", e)
                        

                 
                     
                  case '7':
                    
                    try:
                        if self.df is None:
                            print("Please load the dataset first.")
                            continue

                        print("Available columns:", list(self.df.columns))
                        selected = input("Enter comma-separated column names for heatmap: ")

                        # Split and clean input
                        cols = [col.strip() for col in selected.split(',')]

                        # Check if all selected columns are in the DataFrame
                        if not all(col in self.df.columns for col in cols):
                            print("One or more columns are invalid.")
                            continue

                        # Extract the selected columns
                        selected_df = self.df[cols].select_dtypes(include='number')

                        if selected_df.empty:
                            print("Selected columns do not contain numeric data.")
                            continue

                        # Compute correlation and draw heatmap
                        corr = selected_df.corr()
                        plt.figure(figsize=(10, 6))
                        sns.heatmap(corr, annot=True, cmap='coolwarm', linewidths=0.5)
                        plt.title(f"Heatmap of Selected Columns: {', '.join(selected_df.columns)}")
                        plt.tight_layout()
                        plt.show()

                        self.last_plot = plt
                        self.last_plot_saved = True

                        save = input("Do you want to save this heatmap? (yes/no): ").lower()
                        if save == "yes":
                            file_name = input("Enter the file name (with .png or .jpg): ")
                            try:
                                plt.savefig(file_name)
                                print(f"Heatmap saved as '{file_name}'")
                            except Exception as e:
                                print("Error saving heatmap:", e)

                    except Exception as e:
                        print("Error generating heatmap:", e)



                  case '8':
                     print("Exiting...")
                     break
                 
                  case _:
                     print("Invalid option")


    def dataframe_operations(self):
            if self.df is None:
                print("Please load the dataset first.")
                return

            while True:
                print("\nDataFrame Operations Menu:")
                print("1. Show Info")
                print("2. Show Shape")
                print("3. Show Columns")
                print("4. Rename Column")
                print("5. Drop Column")
                print("6. Exit")

                choice = input("Enter your choice: ")

                match choice:
                    case '1':
                        print(self.df.info())
                    case '2':
                        print("Shape:", self.df.shape)
                    case '3':
                        print("Columns:", list(self.df.columns))

                    case '4':
                        old = input("Enter column to rename: ")
                        new = input("Enter new name: ")
                        if old in self.df.columns:
                            self.df.rename(columns={old: new}, inplace=True)
                            print(f"Renamed '{old}' to '{new}'")
                        else:
                            print("Column not found.")

                    case '5':
                        col = input("Enter column to drop: ")
                        if col in self.df.columns:
                            self.df.drop(columns=[col], inplace=True)
                            print(f"Column '{col}' dropped.")
                        else:
                            print("Column not found.")

                    case '6':
                        print("Exiting DataFrame operations...")
                        break
                    case _:
                        print("Invalid option.")

        

    

            
                         
    
sales = load_data()
print("========= Data Analysis & Visualization Program =========")
while True:
    try:
        print("\n")
        print("1. Load Dataset")
        print("2. Explore Data")
        print("3. Perform DataFrame Operations")
        print("4. Handle Missing Data")
        print("5. Generate Descriptive Statistics")
        print("6. Data Visualization")
        print("7. Exit")
        print("\n")
        choice = input("Enter Your Choice: ")

        match choice:
            case '1':
                try:
                    sales.data()
                except Exception as e:
                    print("Error in loading dataset:", e)

            case '2':
                try:
                    sales.explore_data()
                except Exception as e:
                    print("Error exploring data:", e)

            case '3':
                try:
                    sales.dataframe_operations()
                except Exception as e:
                    print("Error in DataFrame operations:", e)

            case '4':
                try:
                    sales.handle_missing_data()
                except Exception as e:
                    print("Error handling missing data:", e)

            case '5':
                try:
                    sales.descriptive_statistics()
                except Exception as e:
                    print("Error in descriptive statistics:", e)

            case '6':
                try:
                    sales.data_visulaization()
                except Exception as e:
                    print("Error in data visualization:", e)

            case '7':
                print("Thank you! Exiting...")
                break

            case _:
                print("Invalid option")

    except KeyboardInterrupt:
        print("\nInterrupted by user. Exiting...")
        break
    except Exception as e:
        print("An unexpected error occurred in the main loop:", e)                
                        


                    
                    
                
                

                
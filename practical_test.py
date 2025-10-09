import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class RetailAnalyzer:
    def _init_(self):
        self.df = None

    def load_data(self, file_path):
        if not file_path.endswith('.csv'):
            print("\nInvalid file format. Please provide a CSV file.")
            return
        try:
            self.df = pd.read_csv(file_path)
            print("\nData loaded successfully!")
            print(self.df.head())

            # Handle missing values
            missing = self.df.isnull().sum().sum()
            if missing > 0:
                print(f"\nDetected {missing} missing values. Filling with 0.")
                self.df.fillna(0, inplace=True)
        except FileNotFoundError:
            print("\nFile not found.")
        except Exception as e:
            print(f"\nError: {e}")

    def calculate_metrics(self):
        if self.df is None:
            print("\nNo data loaded.")
            return

        print("\nRetail Sales Metrics:")
        print(f"Total Sales: ₹{self.df['Total Sales'].sum():,.2f}")
        print(f"Average Sales: ₹{self.df['Total Sales'].mean():,.2f}")
        most_popular = self.df.groupby('Product')['Quantity Sold'].sum().idxmax()
        print(f"Most Popular Product: {most_popular}")

        daily_sales = self.df.groupby('Date')['Total Sales'].sum().values
        if len(daily_sales) > 1:
            growth = np.diff(daily_sales) / daily_sales[:-1] * 100
            avg_growth = np.mean(growth)
            print(f"Average Daily Growth: {avg_growth:.2f}%")

    def filter_data(self, category=None, start_date=None, end_date=None):
        if self.df is None:
            print("\nNo data loaded.")
            return None
        filtered_df = self.df.copy()
        if category:
            filtered_df = filtered_df[filtered_df['Category'] == category]
        if start_date:
            filtered_df = filtered_df[filtered_df['Date'] >= start_date]
        if end_date:
            filtered_df = filtered_df[filtered_df['Date'] <= end_date]

        print(f"\nFiltered {len(filtered_df)} records.")
        print(filtered_df.head())
        return filtered_df

    def display_summary(self):
        if self.df is None:
            print("\nNo data loaded.")
            return
        print("\nSummary Report:")
        print(self.df.describe(include='all'))

    def visualize(self):
        if self.df is None:
            print("\nLoad data first.")
            return

        while True:
            print("\n--- Visualization Menu ---")
            print("1. Bar Chart: Total Sales by Category")
            print("2. Line Graph: Sales Over Time")
            print("3. Heatmap: Correlation of Features")
            print("4. Pie Chart: Sales Distribution by Product")
            print("5. Box Plot: Price Distribution per Category")
            print("6. Histogram: Quantity Sold Distribution")
            print("7. Scatter Plot: Price vs Quantity Sold")
            print("8. Back to Main Menu")

            choice = input("Choose a plot (1-8): ")

            match choice:
                case '1':
                    try:
                        self.df.groupby('Category')['Total Sales'].sum().plot(kind='bar', title='Total Sales by Category')
                        plt.ylabel('Sales (₹)')
                        plt.tight_layout()
                        plt.show()
                    except Exception as e:
                        print(f"Error in Bar Chart: {e}")

                case '2':
                    try:
                        self.df['Date'] = pd.to_datetime(self.df['Date'], dayfirst=True, errors='coerce')
                        self.df.dropna(subset=['Date'], inplace=True)
                        self.df.groupby('Date')['Total Sales'].sum().plot(kind='line', marker='o', title='Sales Over Time')
                        plt.ylabel('Sales (₹)')
                        plt.xticks(rotation=45)
                        plt.tight_layout()
                        plt.show()
                    except Exception as e:
                        print(f"Error in Line Graph: {e}")

                case '3':
                    try:
                        plt.figure(figsize=(8, 5))
                        sns.heatmap(self.df[['Unit Price', 'Quantity Sold', 'Total Sales']].corr(), annot=True, cmap='coolwarm')
                        plt.title('Correlation Heatmap')
                        plt.tight_layout()
                        plt.show()
                    except Exception as e:
                        print(f"Error in Heatmap: {e}")

                case '4':
                    try:
                        data = self.df.groupby('Product')['Total Sales'].sum()
                        data.plot(kind='pie', autopct='%1.1f%%', title='Sales Distribution by Product')
                        plt.ylabel('')
                        plt.tight_layout()
                        plt.show()
                    except Exception as e:
                        print(f"Error in Pie Chart: {e}")

                case '5':
                    try:
                        plt.figure(figsize=(10, 6))
                        sns.boxplot(x='Category', y='Unit Price', data=self.df)
                        plt.title('Price Distribution by Category')
                        plt.xticks(rotation=45)
                        plt.tight_layout()
                        plt.show()
                    except Exception as e:
                        print(f"Error in Box Plot: {e}")

                case '6':
                    try:
                        plt.hist(self.df['Quantity Sold'], bins=10, edgecolor='black')
                        plt.title('Quantity Sold Distribution')
                        plt.xlabel('Quantity')
                        plt.ylabel('Frequency')
                        plt.tight_layout()
                        plt.show()
                    except Exception as e:
                        print(f"Error in Histogram: {e}")

                case '7':
                    try:
                        plt.scatter(self.df['Unit Price'], self.df['Quantity Sold'], alpha=0.7)
                        plt.xlabel('Unit Price')
                        plt.ylabel('Quantity Sold')
                        plt.title('Price vs Quantity Sold')
                        plt.tight_layout()
                        plt.show()
                    except Exception as e:
                        print(f"Error in Scatter Plot: {e}")

                case '8':
                    print("Returning to Main Menu...")
                    break

                case _:
                    print("Invalid option. Please select from 1 to 8.")


analyzer = RetailAnalyzer()

while True:
        print("\n===== Retail Sales Data Analyzer Menu =====")
        print("1. Load Data")
        print("2. Display Summary")
        print("3. Calculate Metrics")
        print("4. Filter Data")
        print("5. Visualize Data")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        match choice:
            case '1':
                path = input("Enter CSV file path: ")
                analyzer.load_data(path)
            case '2':
                analyzer.display_summary()
            case '3':
                analyzer.calculate_metrics()
            case '4':
                cat = input("Enter category to filter (or leave blank): ")
                start = input("Start date (YYYY-MM-DD) (or leave blank): ")
                end = input("End date (YYYY-MM-DD) (or leave blank): ")
                analyzer.filter_data(cat if cat else None, start if start else None, end if end else None)
            case '5':
                analyzer.visualize()
            case '6':
                print("Exiting... Thank you!")
                break
            case _:
                print("Invalid choice. Please select from 1 to 6.")
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class SalesDashboard:
    def __init__(self):
        self.dataset = None

    def import_data(self, csv_path):
        if not csv_path.endswith('.csv'):
            print("\nOnly CSV files are supported.")
            return
        try:
            self.dataset = pd.read_csv(csv_path)
            print("\nData successfully loaded!")
            print(self.dataset.head())

            # Handle missing values
            total_missing = self.dataset.isnull().sum().sum()
            if total_missing > 0:
                print(f"\nMissing values found: {total_missing}. Filling with 0.")
                self.dataset.fillna(0, inplace=True)
        except FileNotFoundError:
            print("\nFile not found.")
        except Exception as err:
            print(f"\nUnexpected error: {err}")

    def report_insights(self):
        if self.dataset is None:
            print("\nPlease load data first.")
            return

        print("\nKey Sales Metrics:")
        print(f"Total Revenue: ₹{self.dataset['Total Sales'].sum():,.2f}")
        print(f"Average Revenue: ₹{self.dataset['Total Sales'].mean():,.2f}")
        top_item = self.dataset.groupby('Product')['Quantity Sold'].sum().idxmax()
        print(f"Top Selling Product: {top_item}")

        sales_per_day = self.dataset.groupby('Date')['Total Sales'].sum().values
        if len(sales_per_day) > 1:
            growth_rate = np.diff(sales_per_day) / sales_per_day[:-1] * 100
            print(f"Avg Daily Growth: {growth_rate.mean():.2f}%")

    def search_records(self, item_type=None, from_date=None, to_date=None):
        if self.dataset is None:
            print("\nNo data to filter.")
            return None

        subset = self.dataset.copy()
        if item_type:
            subset = subset[subset['Category'] == item_type]
        if from_date:
            subset = subset[subset['Date'] >= from_date]
        if to_date:
            subset = subset[subset['Date'] <= to_date]

        print(f"\n{len(subset)} entries matched your filter.")
        print(subset.head())
        return subset

    def basic_stats(self):
        if self.dataset is None:
            print("\nNo data loaded.")
            return
        print("\nData Summary:")
        print(self.dataset.describe(include='all'))

    def charts(self):
        if self.dataset is None:
            print("\nLoad data before plotting.")
            return

        while True:
            print("\n--- Visualization Options ---")
            print("1. Category-wise Sales Bar Chart")
            print("2. Sales Trend Line Chart")
            print("3. Feature Correlation Heatmap")
            print("4. Product-wise Sales Pie Chart")
            print("5. Category-wise Price Box Plot")
            print("6. Quantity Histogram")
            print("7. Price vs Quantity Scatter")
            print("8. Return to Menu")

            plot_choice = input("Choose an option (1-8): ")

            match plot_choice:
                case '1':
                    try:
                        self.dataset.groupby('Category')['Total Sales'].sum().plot(kind='bar', title='Category-wise Sales')
                        plt.ylabel('₹ Sales')
                        plt.tight_layout()
                        plt.show()
                    except Exception as ex:
                        print(f"Error: {ex}")
                case '2':
                    try:
                        self.dataset['Date'] = pd.to_datetime(self.dataset['Date'], dayfirst=True, errors='coerce')
                        self.dataset.dropna(subset=['Date'], inplace=True)
                        self.dataset.groupby('Date')['Total Sales'].sum().plot(marker='o', title='Sales Over Time')
                        plt.xticks(rotation=45)
                        plt.tight_layout()
                        plt.show()
                    except Exception as ex:
                        print(f"Error: {ex}")
                case '3':
                    try:
                        plt.figure(figsize=(8, 5))
                        sns.heatmap(self.dataset[['Unit Price', 'Quantity Sold', 'Total Sales']].corr(), annot=True, cmap='coolwarm')
                        plt.title('Feature Correlation')
                        plt.tight_layout()
                        plt.show()
                    except Exception as ex:
                        print(f"Error: {ex}")
                case '4':
                    try:
                        pie_data = self.dataset.groupby('Product')['Total Sales'].sum()
                        pie_data.plot(kind='pie', autopct='%1.1f%%', title='Product-wise Sales Share')
                        plt.ylabel('')
                        plt.tight_layout()
                        plt.show()
                    except Exception as ex:
                        print(f"Error: {ex}")
                case '5':
                    try:
                        plt.figure(figsize=(10, 6))
                        sns.boxplot(data=self.dataset, x='Category', y='Unit Price')
                        plt.title('Price Distribution by Category')
                        plt.xticks(rotation=45)
                        plt.tight_layout()
                        plt.show()
                    except Exception as ex:
                        print(f"Error: {ex}")
                case '6':
                    try:
                        plt.hist(self.dataset['Quantity Sold'], bins=10, edgecolor='black')
                        plt.title('Quantity Sold Histogram')
                        plt.xlabel('Quantity')
                        plt.ylabel('Count')
                        plt.tight_layout()
                        plt.show()
                    except Exception as ex:
                        print(f"Error: {ex}")
                case '7':
                    try:
                        plt.scatter(self.dataset['Unit Price'], self.dataset['Quantity Sold'], alpha=0.7)
                        plt.title('Price vs Quantity')
                        plt.xlabel('Unit Price')
                        plt.ylabel('Quantity Sold')
                        plt.tight_layout()
                        plt.show()
                    except Exception as ex:
                        print(f"Error: {ex}")
                case '8':
                    print("Back to main menu.")
                    break
                case _:
                    print("Invalid option. Choose between 1–8.")

# --- MAIN PROGRAM or whatttt ---#

panel = SalesDashboard()

while True:
    print("\n===== Sales Data Dashboard =====")
    print("1. Load CSV Data")
    print("2. Show Summary")
    print("3. Show Key Metrics")
    print("4. Filter/Search Records")
    print("5. Plot Graphs")
    print("6. Exit")

    user_input = input("Enter your choice (1-6): ")

    match user_input:
        case '1':
            path = input("Enter path to CSV file: ")
            panel.import_data(path)
        case '2':
            panel.basic_stats()
        case '3':
            panel.report_insights()
        case '4':
            category = input("Filter by category (or leave blank): ")
            from_dt = input("From date (YYYY-MM-DD) (optional): ")
            to_dt = input("To date (YYYY-MM-DD) (optional): ")
            panel.search_records(category or None, from_dt or None, to_dt or None)
        case '5':
            panel.charts()
        case '6':
            print("Exiting program. Goodbye!")
            break
        case _:
            print("Please enter a valid option (1–6).")

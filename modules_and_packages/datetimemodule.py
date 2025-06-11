from datetime import datetime
import time


def currenrdatetime():
    print("\n--- Current Date & time --- \n")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"current Date and Time:{timestamp}")#current date and time 
    print("="*60)


def difference_of_two_date():
    print("\n--- Differences --- \n")
    date1_str = input("Enter the First Date(YYYY-MM-DD):")#input of date1
    date2_str = input("Enter the Second Date(YYYY-MM-DD):")#input of date2

    date1 = datetime.strptime(date1_str,"%Y-%m-%d")
    date2 = datetime.strptime(date2_str,"%Y-%m-%d")


    difference = abs((date1 - date2).days)#diffrences in days

    print(f"Difference:{difference} days")
    print("="*60)



def custom_date_format():
    print("\n--- Format of Date --- \n")

    # Input date string in custom format
    date1_str = input("Enter the First Date (DD-Mon-YYYY, e.g., 29-May-2025): ")

    # Define custom format (e.g., 29-May-2025)
    custom_format = "%d-%b-%Y"

    # Parse string into datetime object
    try:
        date_obj = datetime.strptime(date1_str, custom_format)

        # Display in another custom format
        formatted_date = date_obj.strftime("%A, %d %B %Y")

        print("Original date string:", date1_str)
        print("Parsed and reformatted date:", formatted_date)
    except ValueError:
        print("Invalid date format. Please use DD-Mon-YYYY (e.g., 29-May-2025).")
    print("="*60)



def simple_stopwatch():
    print("\n--- Stopwatch --- \n")
    input("Press Enter to start...")
    start = time.time()  # Save the current time

    input("Press Enter to stop...")
    end = time.time()  # Save the stop time

    elapsed = end - start  # Calculate difference
    print(f"Time elapsed: {elapsed:.2f} seconds")
    print("="*60)


def simple_countdown(seconds):
    print("\n--- Countdown --- \n")

    while seconds>0:
        print(f"Time's Left:{seconds} seconds")
        time.sleep(1)#wait for 1 second
        seconds-=1
    print(f"Time's up:{seconds} seconds")
    print("="*60)


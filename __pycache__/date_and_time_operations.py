from datetime import datetime
import time

def dt_current():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("Current date and time:", now)

def dt_difference():
    try:
        d1 = input("Enter the first date (YYYY-MM-DD): ")
        d2 = input("Enter the second date (YYYY-MM-DD): ")

        date1 = datetime.strptime(d1, "%Y-%m-%d")
        date2 = datetime.strptime(d2, "%Y-%m-%d")

        diff = abs((date1 - date2).days)
        print(f"Difference in days: {diff}")
    except ValueError:
        print("Please enter the date in proper format (e.g. 2004-04-19)!!")

def format_date_custom():
    now = datetime.now().strftime("%I:%M:%p %d-%m-%Y")
    print(f"Your formatted date: {now}")

def stopwatch():
    try:
        input("Press Enter to start the stopwatch...")
        start = datetime.now()

        input("Press Enter to stop the stopwatch...")
        end = datetime.now()

        diff = end - start
        print("Total seconds elapsed:", diff.total_seconds())
    except Exception as e:
        print("Error occurred in stopwatch:", e)

def countdown_timer(seconds):
    try:
        while seconds > 0:
            mins, secs = divmod(seconds, 60)
            timer = f"{mins:02d}:{secs:02d}"
            print(timer, end="\r")
            time.sleep(1)
            seconds -= 1
        print("Time's up!")
    except ValueError:
        print("Please enter only numbers!")

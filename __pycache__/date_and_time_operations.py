
from datetime import datetime 
import time


def dt_time():
    now = datetime.now().strftime("%y-%m-%d %H:%M:%S")
    print("Current date and time: ",now)

def dt_difference():
    try:
        d1 = input("Enter The First Date: (YYYY-MM-DD): ")
        d2 = input("Enter The Second Date: (YYYY-MM-DD): ")

        date1 = datetime.strptime(d1,"%Y-%m-%d")
        date2 = datetime.strptime(d2,"%Y-%m-%d")

        diff  = abs((date1 - date2).days)
        print(f"Difference days: {diff}")
    except ValueError:
        print("Please enter date in proper format (e.g. 2004-04-19)!!")


def format_date_custom():

    now = datetime.now().strftime("%I:%M:%p %d-%m-%Y")
    print(f" formated date: {now}")

def stopwatch():
   


        input("Press Enter")

        start = datetime.now()
        
        input("Press Enter")
        
        end = datetime.now()
        diff = end - start

        print("Total Seconds: ",diff.total_seconds())
    # except ValueError:
        # print(" ")

def countdown_timer(second):
        try:
            while second > 0:
                mins, secs = divmod(second ,60) 
                timer = f"{mins}:{secs:02d}" 
                print(timer)
                time.sleep(1)
                second -= 1
            print("Time is uppp!!!")
        except ValueError:
            print(" Enter only numbers !!")
    
          


    

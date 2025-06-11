import random
import string



def gerenerate_random_number():
    print("\n--- Random number Generator ---\n")
    #random number generate upto 1 to 1000
    number = random.randint(1,1000)
    print(f"Random number:{number}")
    print("="*60)




def generate_random_list():
    print("\n--- Random List Generator ---\n")
    
    try:
        count = int(input("Enter how many numbers you want in the list: "))
        min_val = int(input("Enter the minimum value: "))
        max_val = int(input("Enter the maximum value: "))

        if min_val > max_val:#if the value is less than
            print("Minimum value can't be greater than maximum value.")
            return
        #generate the number upto min to max
        random_list = [random.randint(min_val, max_val) for _ in range(count)]
        print("Generated Random List:", random_list)
    except ValueError:
        print("Please enter valid integer values.")
    
    print("="*60)





def generate_6_digit_password():
    print("\n--- Password Generator ---\n")

    # Generate a password with 6 random digits (0–9)
    password = ''.join(random.choices(string.digits,k=6))
    print("Generated 6-digit password:", password)
    print("="*60)


def generate_otp():
    print("\n--- otp Generator ---\n")

    try:
        length = int(input("Enter legth that you want for the otp:"))

        if length <4 and length>6:
            print("Password must be between 4 digit to 6 digit ")
            
        #random password generate
        otp = ''.join(random.choices(string.digits, k=length))
        print(f" otp:{otp}")
  
    except ValueError:
        print("Please enter valid integer values.")
    
    print("="*60)



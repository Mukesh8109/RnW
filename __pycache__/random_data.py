
import random
import string

def generate():
    try:
        length = int(input("Enter password lngth: "))
        if length < 4:
            print("Password length should be at least more than 4!")
            return
        character = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choices(character, k=length))
        print("Generated password:", password)
    
    except ValueError:
        print(" ")

def otp_generator():
    r = random.randint(1000,9999)
    return r
    



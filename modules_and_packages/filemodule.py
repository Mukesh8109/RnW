from datetime import datetime



def create_new_file():

    try:
       filename = input("Enter your filename(with .txt extension)(e.g., student.txt):")
       with open(filename,"x") as file:#create the file
          print(f"file {filename} created successfully")
    except FileExistsError:#file does not exit
       print(f"file {filename} already exists")
    print("="*60)


def write_to_file():
    try:#enter the filename to write
      filename = input("Enter the filename to write content:")
      #write the content to the file
      content = input("Enter the content to a file:")
      #current date and time
      timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
      with open(filename,"w") as file:#write mode
         file.write(f"[{timestamp}]\n{content}\n\n")
         print("Data Written successfully")
    except FileNotFoundError as e:#if file does not exit
          print("File not found")     
    except Exception as e:#any exception if occured
          print(f"Exception is occur : {e}")
    print("="*60)


def read_to_file():
    try:
        #enter the filename from the read
        filename = input("Enter the filename to read file:")
        with open(filename,"r") as file:#read mode
            content = file.read()
            print(f"File Content : {content}")
    except FileNotFoundError as e:#if file does not exit
          print("File not found")
    except Exception as e:#any exception if occured
          print(f"Exception is occur : {e}")


def append_to_file():
    try:
      #enter the filename from the read
      filename = input("Enter the filename to write in file:")
      #write the content to the file
      content = input("Enter the content to a file:")
      timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")      #current date and time
      with open(filename,"a") as file:#append mode
         file.write(f"[{timestamp}]\n{content}\n\n")
         print("Written successfully")
    except FileNotFoundError as e:#if file does not exit
          print("File not found")     
    except Exception as e:#any exception if occured
          print(f"Exception is occur : {e}")
    print("="*60)




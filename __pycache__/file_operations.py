def create():
    filename = input("Enter file name to create (with .txt): ").strip()
    if not filename.endswith(".txt"):
        print("File name must end with .txt")
        return None

    try:
        with open(filename, "r"):
            print("File already exists.")
    except FileNotFoundError:
        with open(filename, "w") as f:
            f.write("File created!\n")
        print(f"{filename} created successfully.")
    return filename

def write_file(filename):
    if filename is None:
        print("Invalid filename. Cannot write.")
        return

    text = input("Enter text to write: ")
    with open(filename, "w") as f:
        f.write(text + "\n")
    print("Content written successfully.\n")

def append_file(filename):
    if filename is None:
        print("Invalid filename. Cannot append.")
        return

    while True:
        text = input("Enter text to append (or type 'exit' to stop): ")
        if text.lower() == 'exit':
            print("Stoppedddddddd!!!!! appending.\n")
            break
        with open(filename, "a") as f:
            f.write(text + "\n")
        print("Text appended .\n")

def read(filename):
    if filename is None:
        print("Invalid filename.")
        return

    try:
        with open(filename, "r") as f:
            content = f.read()
            print("\nFile Content:\n" + "-" * 30)
            print(content)
            print("-" * 30)
    except FileNotFoundError:
        print("not found.")

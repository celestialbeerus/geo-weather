def add():
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    print(f"The sum is: {a + b}")

def subtract():
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    print(f"The difference is: {a - b}")

def multiply():
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    print(f"The product is: {a * b}")

def divide():
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    if b != 0:
        print(f"The quotient is: {a / b}")
    else:
        print("Division by zero is not allowed.")

def menu():
    while True:
        print("\nMenu:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            add()
        elif choice == 2:
            subtract()
        elif choice == 3:
            multiply()
        elif choice == 4:
            divide()
        elif choice == 5:
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    menu()

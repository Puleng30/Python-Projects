'''os is a built-in module within python that checks if
a file exists before trying to read from it'''
import os

'''the calculate functions calculates the 2 numbers 
entered with whichever operator chosen by the user'''
def calculate(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        return num1 / num2
    else:
        raise ValueError('Invalid operator')

'''the write_equation function writes the results 
of the equation to the text file'''
def write_equation(num1, num2, operation, result, filename):
    with open(filename, 'a') as file:
        file.write(f'{num1} {operation} {num2} = {result}\n')

'''the read_equations function reads equations from the 
equations.txt text file'''
def read_equations(filename):
    '''the os.path.exists(filename) returns true if filename 
    exists and false if it does not. if i did not import the 
    os module and the user enters a filename that does not exist,
    then the program would crash and return a "FileNotFoundError. 
    With the os module the program checks first if the file 
    exists and is then able to handle the error and request the 
    user to enter a valid filename'''
    if not os.path.exists(filename):
        print(f'{filename} does not exist')
        return
    with open(filename, 'r') as file:
        for line in file:
            print(line.strip())

'''the main function executes the main logic of the program.
here a loop is used to repeatedly prompt the user to input
their choice, which is either 1, 2 or 3. if a user enter anything 
other than 1, 2 or 3, then an error message will pop up and 
prompt the user to input their choice again. here, defensive programming
is used to handle unexpected events and user inputs. here, defensive 
programming checks against invalid operators, uses the try-except
block to catch any errors that may occur when reading equations from
a file, and checks that the file entered exists before reading 
equations from it.'''
def main():
    filename = None
    while True:
        try:
            choice = int(input('Welcome to the calculator application. Enter 1 to calculate, 2 to read equations, or 3 to quit: '))
            if choice == 1:
                if filename is None:
                    filename = input("Enter the name of the text file followed by .txt: ")
                num1 = float(input('Enter first number: '))
                num2 = float(input("Enter second number: "))
                operation = input('Enter operator (+,-,*,/): ')
                if operation == "/":
                    while num2 == 0:
                        print("Cannot divide by zero. Please enter a valid number.")
                        num2 = float(input("Enter second number: "))
                result = calculate(num1, num2, operation)
                print(f'{num1} {operation} {num2} = {result}')
                write_equation(num1, num2, operation, result, filename)
            elif choice == 2:
                if filename is None:
                    print("No file name has been entered yet.")
                else:
                    read_equations(filename)
            elif choice == 3:
                print("Goodbye!")
                break
            else:
                print('Invalid choice')
        except ValueError:
            print('Invalid input')

if __name__ == '__main__':
    main()

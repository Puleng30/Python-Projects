

#=====importing libraries===========

import datetime


def default_menu():

    print("Select one of the following options below:\n" +

                "a - adding a task\n"+

                "va - view all tasks\n"+

                "vm - view my task\n"+

                "e - exit")
    

def admin_menu():

    print("Select one of the following options below: \n" +

             "r - registering a user\n" +

             "s - show statistics\n" +

             "e - exit")


def read_user_names():

    with open('user.txt', 'r') as file:

            usernames = [line.strip().split(',')[0] for line in file]

    return usernames


def register():

     usernames = read_user_names()



     while True:  

        username = input("Please enter a new username: ")

        if username in usernames:

            print("This username already exists, please try again.")

            continue

        password = input("Please enter a new password: ")

        confirm_password = input("Please confirm your new password: ")

        if password == confirm_password:

            with open('user.txt', 'a') as file:

                file.write(f"{username},{password}\n")

                usernames.append(username) ##Does't read new names from files, directly adds to list

            print(f"{username} has been registered successfully!")

             
        else:

            print("The passwords you entered do not match, please try again.")



#====Login Section==================

def login():

    # Creating an empty dictionary to store usernames and passwords

    users = {}

    # Reading user.txt file and storing usernames and passwords in the users dictionary

    with open('user.txt', 'r') as file:

        for line in file:

            user, password = line.strip().split(',')

            users[user] = password



    while True:

        # Requesting user inputs for username and password

        username = input("Please enter your username: ")

        password = input("Please enter your password: ")



        # Validating username and password

        if username in users and password == users[username]:

            print(f"Welcome {username}!")

            return username

        else:

            print("Invalid username or password, please try again.")



def is_admin(username):

     return username == "admin"


def add_task(): 

    username = input("Please enter the username of the person the task is assigned to: ") 

    title = input("Please enter the title of the task: ") 

    description = input("Please enter a description of the task: ") 

    due_date = input("Please enter the due date of the task (YYYY-MM-DD): ") 

    date_assigned = datetime.date.today().strftime('%Y-%m-%d')

    with open('tasks.txt', 'a') as file:

        file.write(f"{username}, {title}, {description}, {date_assigned}, {due_date}, No\n")
    
    return True

        

def view_all_tasks():

        with open('tasks.txt', 'r') as file:

            for line in file:

                username, title, description, date_assigned, due_date, status = line.strip().split(', ')

                print(f"Assigned to: {username}\nTitle: {title}\nDescription: {description}\nDate Assigned: {date_assigned}\nDue Date: {due_date}\nStatus: {status}\n")



def view_my_tasks(username="admin"): 

         with open('tasks.txt', 'r') as file: 

              for line in file: 

                   task = line.strip().split(', ') 

                   if task[0] == username: 

                        print(f"Assigned to: {task[0]}\nTitle: {task[1]}\nDescription: {task[2]}\nDate Assigned: {task[3]}\nDue Date: {task[4]}\nStatus: {task[5]}\n")



def show_statistics():

    print("------------------------")

    with open('user.txt', 'r') as file:

        usernames = [line.strip().split(',')[0] for line in file]

        print("Number of users: ", len(usernames))


    with open('tasks.txt', 'r') as file:

        tasks = [line.strip().split(',')[0] for line in file]

        print("Number of tasks: ", len(tasks))

    print("-----------------------")

      

username = login()

default_menu(); ##Prints by defualt for all users

print()


if username == "admin":

     admin_menu()

user_selection = input()


if user_selection == 'r': 

        register()

elif user_selection == 'a':

    if add_task(): print("The task has been added successfully!")

elif user_selection == 'va':

     view_all_tasks()

elif user_selection == 'vm':

     username = input("Enter username: ")

     view_my_tasks(username)

elif user_selection == "s":

     show_statistics()

     
elif user_selection == 'e':

    print('Goodbye!!!')

    exit()


else:

        print('Invalid input. Please try again.')




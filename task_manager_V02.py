
#==============importing libraries=================
import os
import datetime
from datetime import date

#==============Defining constants==================
USER_FILE = "user.txt"
TASK_FILE = "tasks.txt"
TASK_OVERVIEW_FILE = "task_overview.txt"
USER_OVERVIEW_FILE = "useroverview.txt"

#=============Defining helper functions============

def get_date():
    """
    Helper function to get date from user input in format yyyy-mm-dd
    """
    while True:
        date_str = input("Enter the task due date (yyyy-mm-dd): ")
        try:
            date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
            return date_obj
        except ValueError:
            print("Invalid date format, please try again.")


def load_users():
    """
    Function to load users from USER_FILE and return a dictionary of users
    """
    users = {}
    with open(USER_FILE, "r") as f:
        for line in f:
            username, password = line.strip().split(",")
            users[username] = {"password": password}            
    return users


def save_users(users):
    """
    Function to save users to USER_FILE
    """
    with open(USER_FILE, "a") as f:
        username = users["username"]
        password = users["password"]
        is_admin = str(users["is_admin"])
        f.write(f"{username},{password}\n")
        f.close()


def view_tasks():
    """
    Function to load tasks from TASK_FILE and return a list of tasks
    """
    print("LOADING TASKS")
    with open(TASK_FILE, "r") as f:
        for i, line in enumerate(f):
            task_data = line.strip().split(",")
            print(f"--------- Task {i+1} ---------")
            print(f"Task: {task_data[1]}\nAssigned To: {task_data[0]}\nDate Assigned: {task_data[4]}\nDue Date: {task_data[3]}\nTask Complete? {task_data[5]}\nTask Description: {task_data[2]}\n")

def view_mytasks(username):
    """
    Function to load my tasks from TASK_FILE and return a list of tasks
    """
    print("LOADING MY TASKS")
    with open(TASK_FILE, "r") as f:
        for i, line in enumerate(f):
            task_data = line.strip().split(",")
            if task_data[0].strip()==username:
                print(f"--------- Task {i+1} ---------")
                print(f"Task: {task_data[1]}\nAssigned To: {task_data[0]}\nDate Assigned: {task_data[4]}\nDue Date: {task_data[3]}\nTask Complete? {task_data[5]}\nTask Description: {task_data[2]}\n")

    task_number = input("Enter the task number to edit or mark as complete: ")

    with open(TASK_FILE, "r") as file:
        text = file.readlines()
    target_task=text[int(task_number)-1]
    target_task=text[int(task_number)-1].split(",")

    if username==target_task[0].strip():
        n_action = input("Enter 1 if you would like to mark task as complete or 2 if you would like to edit the task: ")
        if int(n_action) == 1:
            target_task[5] = "Yes\n"
        elif int(n_action) == 2:
            #checking if the task is not completed
            if target_task[5].strip() == "Yes":
                print("Sorry, you cannot edit a completed task.")
            else:
                #editing due date
                due_date = get_date()
                target_task[3] = due_date
                #editing username
                while True:
                    assigned_user = input("Assign task to (username): ")
                    if assigned_user not in load_users():
                        print("Invalid username, please try again.")
                    else:
                        break        
                target_task[0] = assigned_user
        #updating the text to write into the file
        text[int(task_number)-1] = ",".join(map(str,target_task))               
        with open(TASK_FILE, "w") as file:
            for task in text:
                file.write(str(task))
            file.close()
    

def save_tasks(tasks):
    """
    Function to save tasks to TASK_FILE
    """
    with open(TASK_FILE, "w") as file:
        for task in tasks:
            user = task["user"]
            title = task["title"]
            description = task["description"]
            due_date = task["due_date"].strftime("%Y-%m-%d")
            completed = str(task["completed"])
            file.write(f"\n{user},{title},{description},{due_date},{completed}\n")


def reg_user(login_username):
    """
    Function to register a new user
    """ 
    if login_username == "admin":
        print("REGISTER USER")
        users = []
        #opening the users_file
        with open('user.txt') as file:
            for user in file:
                users.append(user.split(",")[0])
        while True:
            username = input("Enter new username: ")
            if username in users:
                print("Username already exists, please try again.")
            else:
                break
        password = input("Enter password: ")
        is_admin = input("Is this an admin user? (y/n)").lower() == "y"
        user_entry = {"username":username, "password": password, "is_admin": is_admin}
        save_users(user_entry)
        print(f"User {username} has been registered.")
    else:
        print("Non admin users are not allowed to register users")

def add_task(users, tasks):
    """
    Function to add a new task
    """
    print("Enter task details:")
    title = input("Title: ")
    description = input("Description: ")
    due_date = get_date()
    current_date = date.today()
    while True:
        assigned_user = input("Assign task to (username): ")
        if assigned_user not in users:
            print("Invalid username, please try again.")
        else:
            break
    with open(TASK_FILE, "a") as file:
        file.write(f"{assigned_user} ,{title} ,{description}, {due_date}, {current_date}, No\n")
        file.close()


def generate_reports():
    print("GENERATE REPORTS\n")
    number_of_tasks = len(open(TASK_FILE,"r").readlines())
    with open(TASK_FILE, "r") as f:
        tasks_completed = 0
        tasks_uncompleted = 0
        tasks_uncompleted_and_overdue = 0
        percentage_uncomplete = 0
        percentage_overdue = 0
        for line in f:
            task_data = line.strip().split(",")
            if task_data[5].strip()=="Yes":
                tasks_completed+=1            
            else:
                if datetime.datetime.strptime(task_data[3].strip(), "%Y-%m-%d") < datetime.datetime.strptime(str(date.today()),"%Y-%m-%d"):
                    tasks_uncompleted_and_overdue+=1                 
        tasks_uncompleted = number_of_tasks-tasks_completed        
        percentage_uncomplete = round((tasks_uncompleted/number_of_tasks)*100,2)
        percentage_overdue = round((tasks_uncompleted_and_overdue/number_of_tasks)*100,2)
        #Creating the task_overview.txt text file
        with open("task_overview.txt","w") as file:
            file.write(f"Total number of completed tasks: {tasks_completed}\nTotal number of uncompleted tasks: {tasks_uncompleted}\nNumber of uncompleted tasks & overdue: {tasks_uncompleted_and_overdue}\nPercentage of incomplete tasks: {percentage_uncomplete}%\nPercentage of overdue tasks: {percentage_overdue}%\n")
            file.close()

    #Creating the useroverview file
    with open("useroverview.txt","w") as output_file:

        n_users = len(load_users())
        output_file.write(f"Total number of users who are registered with task_manager.py: {n_users}\n")
        output_file.write(f"Toal number of tasks generated and tracked using the task_manager.py: {number_of_tasks}\n")
        for user in load_users():
            user_tasks = []
            user_tasks_completed = 0
            user_tasks_uncompleted_overdue = 0

            with open(TASK_FILE, "r") as f:
                for line in f:
                    task_data = line.strip().split(",")
                    if user==task_data[0]:
                        user_tasks.append(task_data)
                        if task_data[5]=="Yes":
                            user_tasks_completed+=1
                        else:    
                            #Checking if task is overdue
                            if datetime.datetime.strptime(task_data[3].strip(), "%Y-%m-%d") < datetime.datetime.strptime(str(date.today()),"%Y-%m-%d"):
                                user_tasks_uncompleted_overdue+=1

                        user_total_tasks = len(user_tasks)   
                        user_tasks_per = round((user_total_tasks/number_of_tasks)*100,2)       
                        user_tasks_completed_per = round((user_tasks_completed/user_total_tasks)*100,2)
                        user_tasks_uncompleted = user_total_tasks-user_tasks_completed
                        user_tasks_uncompleted_per = round((user_tasks_uncompleted/user_total_tasks)*100,2)
                        user_tasks_uncompleted_overdue_per = round((user_tasks_uncompleted_overdue/user_total_tasks)*100,2)
                        output_file.write(f"{user} total tasks: {user_total_tasks}\n")
                        output_file.write(f"Percentage of total tasks assigned to {user} : {user_tasks_per}%\n")
                        output_file.write(f"Percentage of {user} tasks that have been completed: {user_tasks_completed_per}%\n")
                        output_file.write(f"Percentage of {user} tasks that have not been completed: {user_tasks_uncompleted_per}%\n")
                        output_file.write(f"Percentage of {user} tasks that are incomplete and overdue: {user_tasks_uncompleted_overdue_per}%\n")
        output_file.close()

                                                     
def display_stats(username):
    if username=="admin":
        print("STATS DISPLAY\n")
        #Generating files if they do not exist
        if not ((os.path.isfile("useroverview.txt") and os.path.isfile("task_overview.txt"))):
            generate_reports()

        print("TASK OVERVIEW STATS:\n")
        with open(TASK_OVERVIEW_FILE,"r") as f:
            for line in f:
                print(line.rstrip())

        print("\nUSER OVERVIEW STATS:\n")
        with open(USER_OVERVIEW_FILE,"r") as f:
            for line in f:
                print(line.rstrip())
    else:
        print("Non admin users are not allowed to display statistics")

#====Login Section==================
def login():
    print("LOGIN")
    username = input("Enter your username: ")

    usernames = []
    passwords = []
    #opening the users_file
    with open('user.txt') as file:
        for user in file:
            usernames.append(user.split(",")[0])
            passwords.append(user.split(",")[1])       
    if username in usernames:
        input_password = input("Enter your password: ")
        user_password = passwords[usernames.index(username)].strip()

        if input_password == user_password:
            if username == "admin":
                print("Select one of the following options below:\n" +

                                "r - register a user\n"+

                                "a - adding a task\n"+

                                "va - view all tasks\n"+

                                "vm - view my task\n"+

                                "gr - generate reports\n"+
                                
                                "ds - display statistics\n"+

                                "e - exit")
            else:
                print("Select one of the following options below:\n" +

                                "a - adding a task\n"+

                                "va - view all tasks\n"+

                                "vm - view my task\n"+

                                "gr - generate reports\n"+

                                "e - exit")
                                
            option = input("Enter one of the options from the menu: ")

            if option == "r":
                reg_user(username)
            elif option == "a":
                add_task(load_users(),view_tasks())
            elif option == "va":
                view_tasks()
            elif option == "vm":
                view_mytasks(username)
            elif option == "gr":
                generate_reports()
            elif option == "ds":
                display_stats(username)
            elif option == "e":
                print("Bye")    
        else:
            print("Invalid password, please enter the correct password")   
    else:
        print("Username does not exist, please enter a valid username")
login()



'''Please clarify what you mean by: "When generating reports remember to display the task statistics of 
each user in the users.txt file." My understanding is that the user.txt file is only supposed to contain 
usernames and passwords of users? Or did you mean usersoverview.txt file? If so, I think the information 
is already there, unless I am misunderstanding what you.
Please clarify, thank you''' 
# import libraries
import re
from datetime import datetime
#import datetime

# Login Function
# Here I write code that will allow a user to login.
def login():
    user_dict = {}  # - Create a dictionary to store a list of usernames and passwords from the file.
    with open("user.txt", "r") as f:  # - read usernames and password from the user.txt file
        for line in f:
            (key, val) = line.split(', ')
            new_val = re.sub('\n', '', val)
            user_dict[key] = new_val

    while True:  # - Use a while loop to validate username and password
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        # - Check if the username of the person logged in is the same as the username I have
        if username in user_dict and user_dict[username] == password:
            print("Login Successful!")
            return username
        elif input("Incorrect username or password. Enter '#' to exit the program: ") == "#":
            return '#'
        else:
            print("Incorrect username or password. Please try again.\n")


# Registering a user function
# In this block I will write code to add a new user to the user.txt file
# Register a new user
def reg_user():
    user_dict = {}
    with open("user.txt", "r") as f:  # Load the data into user_dict
        for line in f:
            (key, val) = line.split(', ')
            new_val = re.sub('\n', '', val)
            user_dict[key] = new_val

    while True:  # user and password verification
        username = input("Enter a new username: ")
        if username in user_dict:  # verify if username already exists
            print("Username already exists. Please try a different username.")
        else:
            password = input("Enter a new password: ")
            confirm_password = input("Confirm your password: ")
            if password == confirm_password:
                with open("user.txt", "a") as f:
                    f.write(username + ", " + password + "\n")
                    print("User registered successfully!")
                    break
            else:
                print("Passwords do not match. Please try again.")


# Adding a task function
# In this block I will put code that will allow a user to add a new task to task.txt file
# Add a new task
def add_task():
    task_dict = {}
    with open("tasks.txt", "r") as f:  # Load the data into task_dict
        for line in f:
            (key, val) = line.split(', ')
            new_val = re.sub('\n', '', val)
            task_dict[key] = new_val

    while True:  # Ask and Verify if  task is in task_dict
        task_name = input("Enter a task name: ")
        if task_name in task_dict:
            print("Task name already exists. Please try a different task name.")
        else:  # Add task_description assignee due_date into tasks.txt
            task_description = input("Enter a task description: ")
            assignee = input("Enter the assignee's username: ")
            due_date = input("Enter the due date ( 10 Oct 2019 - %d %b %Y): ")
            with open("tasks.txt", "a") as f:
                f.write(task_name + ", " + task_description + ", " + assignee + ", " + due_date + ", No\n")
                print("Task added successfully!")
                break


# View all tasks function
# In this block I will put code so that the program will read the task from task.txt file
def view_all():
    with open("tasks.txt", "r") as f:  # - Read a line from the file.
        lines = f.readlines()
        if lines:
            for line in lines:
                task = line.strip().split(", ")  # - Split that line where there is comma and space.
                # print to the console in the format of Output 2 presented in the L1T19 pdf file page 6
                print(
                    f"Task Name: {task[1]}\nAssigned to: {task[0]}\nDate assigned: {task[3]}\nDue date: {task[4]}\nStatus: {task[5]}\n")
        else:
            print("No tasks found!\n")


# View my tasks function
# In this block I will put code the that will read the task from task.txt file and
def view_mine(user):
    task_dict = {}
    with open("tasks.txt", "r") as f:  # Read tasks.txt and Load the data into task_dict
        for line in f:
            task_id, task_desc, assigned_to, due_date, completed, date_completed = map(str.strip, line.split(","))
            if assigned_to == user:
                task_dict[task_id] = (task_desc, assigned_to, due_date, completed, date_completed)

    while True:  # Display all tasks in a manner that is easy to read.
        print("Tasks assigned to you:")
        for i, (task_id, task) in enumerate(task_dict.items(), start=1):
            print(f"{i}. Task: {task[0]}")
            print(f"   Description: {task[0]}")
            print(f"   Assigned to: {task[1]}")
            print(f"   Due date: {task[2]}")
            print(f"   Completed: {task[3]}")
            print()

        choice = input("Enter task number to edit/mark as complete, or '-1' to return to main menu: ")
        if choice == '-1':
            break
        # Allow the user to select either a specific task (by entering a number) or input '-1' to return to the main menu.
        try:
            task_num = int(choice) - 1
            if task_num < 0 or task_num >= len(task_dict):
                print("Invalid task number, please try again")
                continue
        except ValueError:
            print("Invalid input, please try again")
            continue

        task_id = list(task_dict.keys())[task_num]
        task = task_dict[task_id]

        print(f"Selected task: {task_id}")
        print(f"Task: {task[0]}")
        print(f"Description: {task[0]}")
        print(f"Assigned to: {task[1]}")
        print(f"Due date: {task[2]}")
        print(f"Completed: {task[3]}")

        # Verify if task is complete,f no complete it
        sub_choice = input("Enter 'c' to mark task as complete, 'e' to edit task, or any other key to cancel: ")
        if sub_choice == 'c':
            if task[3] == 'Yes':
                print("This task has already been completed")
            else:
                task_dict[task_id] = (task[0], task[1], task[2], 'Yes', task[4])
                with open("tasks.txt", "r") as f:
                    lines = f.readlines()
                with open("tasks.txt", "w") as f:
                    for line in lines:
                        if line.startswith(task_id):
                            f.write(f"{task_id}, {task[0]}, {task[1]}, {task[2]}, Yes, {task[4]}\n")
                        else:
                            f.write(line)
                print("Task marked as complete")

        # Verify if Yes, task has already been completed
        elif sub_choice == 'e':
            if task[3] == 'Yes':
                print("This task has already been completed and cannot be edited")
            else:
                new_assigned_to = input("Enter new username for task (leave blank to keep current): ")
                new_due_date = input("Enter new due date '%Y-%m-%d' for task (leave blank to keep current): ")
                if new_assigned_to or new_due_date:
                    task_dict[task_id] = (
                    task[0], new_assigned_to or task[1], new_due_date or task[2], task[3], task[4])
                    with open("tasks.txt", "r") as f:
                        lines = f.readlines()
                    with open("tasks.txt", "w") as f:
                        for line in lines:
                            if line.startswith(task_id):
                                f.write(f"{task_id}, {task[0]}, {task[1]}, {task[2]}, Yes, {task[4]}\n")
                        else:
                            f.write(line)
                print("Task has already been completed")


# Generate user overview report function
def generate_reports():
    total_tasks = 0
    completed_tasks = 0
    uncompleted_tasks = 0
    overdue_tasks = 0
    user_dict = {}

    # Count tasks and calculate task-related statistics
    with open("tasks.txt", "r") as f:
        for line in f:
            total_tasks += 1
            print(line)
            (task, description, user, date_assigned, due_date, status) = line.split(", ")
            status = status.strip()
            if status == "Yes":
                completed_tasks += 1
            else:
                uncompleted_tasks += 1
                due_date = datetime.strptime(due_date, '%d %b %Y').date()
                if due_date < datetime.today().date():
                    overdue_tasks += 1

    # Write task overview report to file
    with open("task_overview.txt", "w") as f:
        f.write("Task Overview Report\n\n")
        f.write(f"Total number of tasks: {total_tasks}\n")
        f.write(f"Total number of completed tasks: {completed_tasks}\n")
        f.write(f"Total number of uncompleted tasks: {uncompleted_tasks}\n")
        f.write(f"Total number of tasks that are overdue: {overdue_tasks}\n")
        f.write(f"Percentage of tasks that are incomplete: {round(uncompleted_tasks / total_tasks * 100, 2)}%\n")
        f.write(f"Percentage of tasks that are overdue: {round(overdue_tasks / total_tasks * 100, 2)}%\n")

    # Count tasks for each user and calculate user-related statistics
    with open("tasks.txt", "r") as f:
        for line in f:
            (task, description, user, date_assigned, due_date, status) = line.split(", ")
            status = status.strip()
            if user in user_dict:
                user_dict[user][0] += 1
                if status == "Yes":
                    user_dict[user][1] += 1
                else:
                    due_date =  datetime.strptime(due_date, '%d %b %Y').date()
                    if due_date < datetime.today().date():
                        user_dict[user][2] += 1
            else:
                user_dict[user] = [1, 0, 0]
                if status == "Yes":
                    user_dict[user][1] += 1
                else:
                    due_date =  datetime.strptime(due_date, '%d %b %Y').date()
                    if due_date < datetime.today().date():
                        user_dict[user][2] += 1

    # Write user overview report to file
    with open("user_overview.txt", "w") as f:
        f.write("User Overview Report\n\n")
        f.write(f"Total number of users: {len(user_dict)}\n")
        f.write(f"Total number of tasks: {total_tasks}\n")
        for user, data in user_dict.items():
            task_count = data[0]
            task_percentage = round(task_count / total_tasks * 100, 2)
            complete_percentage = round(data[1] / task_count * 100, 2) if task_count != 0 else 0
            incomplete_percentage = round((task_count - data[1]) / task_count * 100, 2) if task_count != 0 else 0
            overdue_percentage = round(data[2] / task_count * 100, 2) if task_count != 0 else 0

            f.write(f"\nUser: {user}\n")
            f.write(f"Total tasks assigned: {task_count}\n")
            f.write(f"Percentage of total tasks assigned: {task_percentage}%\n")
            f.write(f"Percentage of tasks completed: {complete_percentage}%\n")
            f.write(f"Percentage of tasks incomplete: {incomplete_percentage}%\n")
            f.write(f"Percentage of tasks overdue: {overdue_percentage}%\n")

    print("User overview report generated successfully.")


# Show Statistics function
# In this block I will read "tasks.txt" and "user.txt" then count the total_task and total_users
def show_stat():
    total_task = 0
    total_users = 0

    try:
        with open("task_overview.txt", "r") as f:
            task_lines = f.readlines()
        with open("user_overview.txt", "r") as f:
            user_lines = f.readlines()
    except FileNotFoundError:
        generate_reports()
        with open("task_overview.txt", "r") as f:
            task_lines = f.readlines()
        with open("user_overview.txt", "r") as f:
            user_lines = f.readlines()

    print("\n----TASK OVERVIEW----\n")
    for line in task_lines:
        print(line.strip())
    print("\n----USER OVERVIEW----\n")
    for line in user_lines:
        print(line.strip())

    with open("tasks.txt", "r") as f:  # - Read a line from the file
        lines = f.readlines()
        total_task = len(lines)  # get the total of task

        if lines:
            pass
        else:
            print("No tasks found!\n")

    with open("user.txt", "r") as f:  # - Read a line from the file
        lines = f.readlines()
        total_users = len(lines)  # get the total of users

        if lines:
            pass
        else:
            print("No users found!\n")
    # Presenting the statistics
    print(f" Statistics ::::  Total task: {total_task} &  Total users: {total_users}")


# Main_menu program
# presenting the menu to the user
def main_menu(user_name):
    while True:

        if user_name == "admin":
            registration = " r - registering a user \n"
            menu_option = " ds - display statistics \n"
        else:
            registration = ""
            menu_option = ""

        menu = input(  # # making sure that the user input is converted to lower case.
            "Please select one of the following options: \n" + registration + menu_option + " a - adding a task\n va - view all tasks\n vm - view my tasks\n gr - generate reports\n  e - exit\n: ").lower()
        if (menu == "r") and (user_name == "admin"):
            reg_user()
        elif (menu == "ds") and (user_name == "admin"):
            show_stat()
        elif menu == "a":
            add_task()
        elif menu == "va":
            view_all()
        elif menu == "vm":
            username = login()
            view_mine(username)
        elif menu == "gr":
            generate_reports()
        elif menu == "e":
            print("Goodbye!!!")
            break
        else:
            print("You have made a wrong choice, Please Try again\n")


# Starts Program calling the login function
user_name = login()

# Verify if user entered #
if user_name == '#':
    print("Goodbye!!!")
    pass
else:
    main_menu(user_name)

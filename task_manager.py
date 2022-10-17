# a program that helps managed assigned
# tasks to a team in a small business
# create an empty list for users and passwords
users = []
passwords = []
# open user file using read function
user_file = open("user.txt", "r")
data = user_file.readlines()
for lines in data:
    username, password = lines.strip("\n").split(", ")
    users.append(username)
    passwords.append(password)

# close file
user_file.close()

# Ask the user to enter a username and if the username is not in the list of users,
# while loop will create error message
username_choice = input("Enter your username: ").lower()
while not username_choice in users:
    username_choice = input("Invalid user, enter your username: ").lower()

# ask user to enter password and if the password is not in the list of passwords,
# while loop will create an error message
password_choice = input("Enter your password: ")
while not password_choice in passwords:
    password_choice = input("Invalid password, enter your password: ")

while True:
    menu = input('''Select one of the following Options below:
        r - Registering a user
        a - Adding a task
        va - View all tasks
        vm - view my task
        d - display statistics
        e - Exit
        : ''').lower()

    # if user selects "r" add a new user to the user.txt file

    if menu == 'r':
        if username_choice == 'admin':
            # Request input of a new username
            new_user = input("Enter your new user name: ")

            # Request input of a new password
            new_pass = input("Enter your new password: ")

            # Request input of password confirmation.
            pass_conf = input("Please confirm your password: ")

            # while loop to Check if the new password and confirmed password are the same and if user is admin.
            # If they are the same and user is admin, add them to the user.txt file,
            # Otherwise you present a relevant message.
            while True:
                if new_pass == pass_conf:
                    with open("user.txt", "a+") as user_file:
                        user_file.write(f"\n{new_user}, {new_pass}")
                        break
                else:
                    pass_conf = input("passwords not the same, please confirm your password: ")
        else:
            print("You are not admin, you cannot register a new user")
    # if statement for if admin and menu option d is entered
    elif menu == 'd' and username_choice == 'admin':

        # initialise task and user number variables to 0
        tasks_num = 0
        users_num = 0

        # open file and add 1 into task num variable per line
        with open("tasks.txt", "r") as total:
            for line in total:
                tasks_num += 1
        print(f"The total number of tasks are: {tasks_num}")

        # open file and add 1 into user num variable per line
        with open("user.txt", "r") as total_users:
            for lines in total_users:
                users_num += 1
        print(f"Total number of users is: {users_num}")


    # if user selects "a" option, allow a user to add a new task to task.txt file
    elif menu == 'a':

        # - A username of the person whom the task is assigned to,
        assigned_to = input("Enter who task is for: ")
        # - A title of a task,
        task_name = input("Enter the task name: ")
        # - A description of the task
        description = input("Enter a brief description of the task: ")
        # - the due date of the task.
        due_date = input("Enter due date of task: ")
        # - Then get the current date.
        date = input("Enter current date: ")

        # - Add the data to the file task.txt
        with open("tasks.txt", "a+") as task_file:
            task_file.write(f"\n{assigned_to}, {task_name}, {description}, {date}, {due_date}, No")

    # if user selects "va" read the task from task.txt file and
    # print to the console in the format of Output 2 presented in the L1T19 pdf file page 6
    elif menu == 'va':

        # - Read a line from the file.
        with open("tasks.txt", "r+") as task_file1:
            for lines in task_file1:
                # - Split that line where there is comma and space.
                task_data = lines.strip("\n").split(", ")
                print(task_data)
                # - Then print the results in the format shown in the Output 2 in L1T19 pdf
                print(f'''Task: \t {task_data[1]}\nAssigned to: \t {task_data[0]}\nDate assigned:\t{task_data[4]}\n
Due Date:\t {task_data[3]}\nTask complete: \t {task_data[5]}\nTask Description: \t {task_data[2]}''')

        # if user selects "v" read the task from task.txt file and
        # print to the console in the format of Output 2 presented in the L1T19
    elif menu == 'vm':

        # - Read a line from the file
        with open("tasks.txt", "r+") as task_file2:

            # - Check if the username of the person logged in is the same as the username you have
            # read from the file.
            # check = input("Confirm your username: ")
            for lines in task_file2:
                # - Split that line where there is comma and space.
                assigned_to, task_name, description, date, due_date, complete = lines.split(", ")
                # - If they are the same you print the task in the format of output 2 shown in L1T19 pdf
                if username_choice == assigned_to:
                    print(
                        f'Task: \t {task_name}\nAssigned to: \t {assigned_to}\nDate assigned:\t{date} Due Date:\t {due_date}\nTask complete: \t {complete}Task Description: \t {description}\n')

    # else if user selects e print goodbye and exit
    elif menu == 'e':
        print('Goodbye!!!')
        exit()
        # else if user selects something outside of menu print relecant statement
    else:
        print("You have made a wrong choice, Please Try again")

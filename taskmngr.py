import datetime

# Function to collect and save user information
def user_information(Ussnm, Passwd):
    name = input("Enter your name: ")
    address = input("Enter your address: ")
    age = input("Enter your age: ")
    filename = Ussnm + "Task.txt"

    with open(filename, 'a') as f:
        f.write(Passwd + '\n')
        f.write("Name: " + name + '\n')
        f.write("Address: " + address + '\n')
        f.write("Age: " + age + '\n')

# Function to sign up a new user
def signup():
    print("Please enter the username you wish to use for your account: ")
    username = input("Please enter your username here: ")
    password = input("Enter password: ")
    user_information(username, password)
    print("Proceed to login")
    login()

# Function to log in an existing user
# Test Merge Test
def login():
    usr_nm = input("Enter your username: ")
    pass_wr = input("Enter password: ") + '\n'
    filename = usr_nm + "Task.txt"

    try:
        with open(filename, 'r') as f_:
            k = f_.readline()

        if pass_wr == k:
            print("1--To view your data \n2--To add tasks \n3--Update task \n4--View task status")
            a = input("Enter your choice: ")
            if a == '1':
                view_data(filename)
            elif a == '2':
                task_information(filename)
            elif a == '3':
                task_update(usr_nm)
            elif a == '4':
                task_update_viewer(usr_nm)
            else:
                print("Wrong input, Please try again.")
        else:
            print("The password or username you entered is incorrect. Please try again.")
            login()
    except Exception as e:
        print("Error:", e)
        login()

# Function to view user data
def view_data(username):
    with open(username, 'r') as ff:
        print(ff.read())

# Function to add tasks
def task_information(username):
    print("Enter the number of tasks you want to add: ")
    j = int(input())
    with open(username, 'a') as f1:
        for i in range(1, j + 1):
            task = input("Enter the task: ")
            target = input("Enter the target: ")
            f1.write(f"Task {i}: {task}\n")
            f1.write(f"Target {i}: {target}\n")
            print("Press the spacebar if you do not wish to continue")
            s = input()
            if s == ' ':
                break

# Function to update task status
def task_update(username):
    filename = username + "Task.txt"
    print("Please enter which task is completed: ")
    
    task_completed = input()
    print("Enter the task that has not been started yet: ")
    task_not_started = input()
    print("Enter ongoing task: ")
    task_ongoing = input()

    with open(filename, 'a') as fw:
        DT = str(datetime.datetime.now())
        fw.write(DT + "\n")
        fw.write("Completed Task\n" + task_completed + "\n")
        fw.write("Ongoing Task\n" + task_ongoing + "\n")
        fw.write("Task not yet started\n" + task_not_started + "\n")

# Function to view task updates
def task_update_viewer(username):
    filename = username + "Task.txt"
    with open(filename, 'r') as o:
        print(o.read())

# Main entry point
if __name__ == '__main__':
    print("Welcome to your personal Task Manager")
    print("Hello! Are you new to this software?")
    a = int(input("If you are a new user, type 1, otherwise hit 0: "))

    if a == 1:
        signup()
    elif a == 0:
        login()
    else:
        print("You have provided the wrong input!")
        
        
# fix the code and make sure that each output corresponds to what who
# test test test

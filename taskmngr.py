import datetime

# Ussm means username, Psswd means password
def user_information(Ussnm, Passwd):
  name = input("Enter your name: ")
  address = input("Enter your address: ")
  age = input("Enter your age: ")
  Ussm_ = Ussnm+" task.txt"

f = open(Ussnm_, 'a')
f.write(Psswd)
f.write("\nName: ")
f.write(name)
f.write('\n')
f.write("Address: ")
f.write(address)
f.write('\n')
f.write("Age: ")
f.write(age)
f.write('\n')
f.close()

def signup():
  print("Please enter the username you wish to use for your account: ")
  username = input("Please enter your username here: ")
  password = input("Enter password: ")
  user_information(username, password)
  print("Proceed to login")
  login()

def login():
  print("Please enter your username: ")
  usr_nm = input("Enter here: ")
  
  # password as entered while logging in
  pass_wr = (input("Enter password: "))+'\n'
  try:
    usernm = user_nm+" task.txt"
    f_ = open(usernm, 'r')

    # variable 'k' contains the password as saved
    # in the files

    k = f_.readlines(0)[0]
    f_.close()

    

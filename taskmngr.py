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


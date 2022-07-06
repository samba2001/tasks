import random
import string 
def get_password(length):
    special_characters="!@#$%^*)(_+=~?"
    characters=list(string.ascii_letters)+list(string.digits)+list(special_characters)
    password=""
    for i in range(length):
        password+=random.choice(characters)
    print(password)
try:
    length=abs(int(input("enter the length of password")))
except:
    print("enter a valid input")
get_password(length)

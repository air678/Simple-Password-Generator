#Simple Password Generator by Airop
import string
import random

def gen_pass(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def menu():
    print(r'''
  _____                                    _    _____                           _             
 |  __ \                                  | |  / ____|                         | |            
 | |__) |_ _ ___ _____      _____  _ __ __| | | |  __  ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
 |  ___/ _` / __/ __\ \ /\ / / _ \| '__/ _` | | | |_ |/ _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
 | |  | (_| \__ \__ \\ V  V / (_) | | | (_| | | |__| |  __/ | | |  __/ | | (_| | || (_) | |   
 |_|   \__,_|___/___/ \_/\_/ \___/|_|  \__,_|  \_____|\___|_| |_|\___|_|  \__,_|\__\___/|_|   
                                                                                              
                                                                                              
''')
    print("1. Generate Password")
    
    options = input("Enter the number of your choice (press 1 to generate passowrd): ")
    
    if options == '1':
        try:
            length = int(input("Enter the length of the password :"))
            if length > 0:
                password = gen_pass(length)
                print("Generated Password :" + password)
                print("Thank you for using my password generator :)")
            else :
                print("Please enter a valid number greater than 0.")
        except ValueError:
            print("Invalid input! Please enter correct number.")
    else :
        print("Invalid choice...Exiting.....")

menu()

from validate_password import validate_pwd
import os
import random

def generate_AZ():
    random_ = random.randint(65,90)
    char = chr(random_)
    return char

def generate_az():
    random_ = random.randint(97,122)
    char = chr(random_)
    return char

def generate_09():
    random_ = random.randint(48,57)
    char = chr(random_)
    return char

def generate_special():
    random_ = random.randint(33,47)
    char = chr(random_)
    return char

def random_password():
    pwd = ""
    for i in range(0,3):
        password = generate_AZ()
        pwd += password
    for i in range(0,3):
        password = generate_09()
        pwd += password
    for i in range(0,3):
        password = generate_az()
        pwd += password
    for i in range(0,3):
        password = generate_special()
        pwd += password

    os.system('clear')
    print(f"Ditt lösenord är \033[1m{pwd}\n")
    check = validate_pwd(pwd)
    return check

def main():
    os.system('clear')
    print("Välkommen till DV1574WebApps lösenordsvalidering.")
    go_on = False
    while not go_on:
        print("-------------------------------------------------")
        choice = int(input("[1] Välj själv ett lösenord \n[2] Får ett godkänt lösenord\nVälj: "))
        if choice == 1:
            string = input("\nVälj ett lösenord:\033[1m ")
            print("\033[0m")
            check = validate_pwd(string)
            go_on = check
        elif choice == 2:
            go_on = random_password()
        else:
            print("\n\t\033[33m Välj mellan 1-2\n\033[37m")


if __name__  ==  "__main__" :
    
    main()
    


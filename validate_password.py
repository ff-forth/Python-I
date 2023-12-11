# Jah har tänkt att det kommer ta runt 12 timmar, fyra timmar arbete i tre dagar. 
# men det tar runt 10 timmar för att vara klart med uppgiften.

import os
def string_length(string):
    """Räkna längden på en sträng
    parameter : string
    returnerar : längden son tal
    """
    length = 0
    for item in string:
        length += 1
    return length

def check_length(string):
    """Vailderar om längen är godkänd
    parameter : string
    returvärde : bool
        sant - om längden är mellan 6-16
        falsk - om längden är mindre än 6 och större än 16
    """
    length = string_length(string)
    if 6 <= length <= 16:
        return True
    elif length < 6:
        print("\t\t\033[33m För kort!\nLösenordet duger inte, vänligen försök igen!\n\033[37m")
        #print("Lösenordet duger inte, vänligen försök igen!")
    else:
        print("\t\t\033[33m För lång!\nLösenordet duger inte, vänligen försök igen!\n\033[37m")
        # print("Lösenordet duger inte, vänligen försök igen!")
    return False

def check_åäö(string):
    """kontrollerar att strängen inte innehåller åäö
    parameter : string
    returvärde : bool
        sant - om strängen inte är åäö
        falsk - om strängen är åäö
    """
    for item in string:
        if 32 > ord(item) or ord(item) > 127:
            print("\033[33m Lösenordet duger inte, vänligen försök igen! \n\tOBS! å, ä, ö är inte tillåtna.\n\033[37m")
            return False
    return True

def check_item(string):
    """Räkna om lösenord uppfyller krav"""
    a_z, A_Z, number, special = 0,0,0,0
    for item in string:
        if 'a' <= item <= 'z':
            a_z += 1
        elif 'A' <= item <= 'Z':
            A_Z += 1
        elif '0' <= item <= '9':
            number += 1
        else:
            special += 1
    return a_z, A_Z, number, special

def requirement(a_z, A_Z, number, special):
    """Informera lösenordets krav"""
    if a_z == 0:
        print("\033[31m Lösenordet måste ha minst en liten bokstav.\033[37m")
    else:
        print("\033[32m Lösenordet måste ha minst en liten bokstav.\033[37m")
    if A_Z == 0:
        print("\033[31m Lösenordet måste ha minst en STOR bokstav.\033[37m")
    else:
        print("\033[32m Lösenordet måste ha minst en STOR bokstav.\033[37m")
    if number == 0:
        print("\033[31m Lösenordet måste ha minst ett numeriskt tecken (siffra).\033[37m")
    else:
        print("\033[32m Lösenordet måste ha minst ett numeriskt tecken (siffra).\033[37m")
    if special == 0:
        print("\033[31m Lösenordet måste ha minst ett av specialtecknen $, @, ! och *.\033[37m")
    else:
        print("\033[32m Lösenordet måste ha minst ett av specialtecknen $, @, ! och *.\033[37m")


def validate_pwd(string):
    check = check_length(string)
    if check == True:
        check = check_åäö(string)
        if check == True:
            a_z, A_Z, number, special = check_item(string)
            if a_z > 0 and  A_Z > 0 and number > 0 and special > 0:
                print("\t\033[32m Bra val!\n\033[37m")
                print("Programmet avslutas...\n")
                return True
            else:
                # print("Lösenordet duger inte, vänligen försök igen!")
                print("\033[33m Lösenordet duger inte, vänligen försök igen och följ kravet!\n\033[37m")
                requirement(a_z, A_Z, number, special)   
                return False
        else:
            return False
    else:
        return False

def main():
    os.system('clear')
    print("Välkommen till DV1574WebApps lösenordsvalidering.")
    go_on = False
    while not go_on:
        print("-------------------------------------------------")
        string = input("Välj ett lösenord:\033[1m ")
        print("\033[0m")
        check = validate_pwd(string)
        go_on = check

if __name__  ==  "__main__" :
    main()

#Version: 1.0
#Coded By MysteriousCode0

from random import randint
import numbers
import os

n3 = 0
n8 = ""

def GeneratePasswords(n3, n8):
    n1 = ""
    n2 = ""
    while True:
        if len(n1) == n3:
            print("[*] " + n1)
            break
        else:
            n0 = randint(0,10)
            if n0 >= 0 and n0 <= 5 and n8 == "Y" or n8 == "y":
                n2 = randint(49,57)
                n1 = n1 + chr(n2)
            else:
                n2 = randint(97,122)
                n1 = n1 + chr(n2)

def GeneratePins():
    n1 = ""
    n2 = ""
    while True:
        if len(n1) == 4:
            print("[*] " + n1)
            break
        else:
            n2 = randint(49,57)
            n1 = n1 + chr(n2)

def Pins():
    os.system("cls")
    b = int(input("[*] How Many Pins?![1: 30] -> "))
    if isinstance(b, numbers.Integral) and b <= 30 and b >= 1:
        print("[*] There Are " + str(b) + " Random Pins For You!")
        for i in range(b):
            GeneratePins()
    elif isinstance(b, numbers.Integral) != True:
        print("[*] Please, Insert Only Numbers!")
    elif b == 0:
        print("[*] You Can't Generate 0 Pins!")
    else:
        print("[*] You Can't Generate More Then 30 Pins!")

def Password():
    os.system("cls")
    try:
        a = int(input("[*] How Many Password?![1: 30] -> "))
    except:
        print("[*] Please, Insert Only Numbers!")
        exit()
    if a == 0:
        print("[*] You Can't Generate 0 Password!")
        exit()
    elif a > 30:
        print("[*] You Can't Generate More Then 30 Passwords!")
        exit()
    n3 = int(input("[*] How Many Long Should Them Be?[1: 10] -> "))
    if n3 > 10:
        print("[*] You Can't Generate A Password More Then 10 Words!")
        exit()
    elif n3 == 0:
        print("[*] You Can't Generate A Password With 0 Words!")
        exit()
    n8 = input("[*] Do You Want Alphanumeric Passwords?[Y/N] -> ")
    if n8 != "Y" and n8 != "N" and n8 != "y" and n8 != "n":
        print("[*] " + n8 + " Isn't A Good Answer!")
        exit()
    print("[*] There Are " + str(a) + " Random Passwords For You!")
    for i in range(a):
        GeneratePasswords(n3, n8)

def Main():
    os.system("cls")
    yn = input("[*] Do You Want Generate Passwords Or Pins?![Pass/Pins] -> ")
    yn = yn.lower()
    if yn == "pass":
        Password()
    elif yn == "pins":
        Pins()
    else:
        print("[*] Sorry, I Don't Understand...")

if __name__ == '__main__':
    Main()

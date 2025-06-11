import time
import datetime
from time import sleep

#the calculator is the only thing that works :/

while True:
    print("starting up please wait...")
    memory1 = 0
    print("set memory1 to 0 sucessfully")
    memory2 = 0
    print("set memory2 to 0 sucessfully")
    memory3 = 0
    print("set memory3 to 0 sucessfully")
    memory4 = 0
    print("set memory4 to 0 sucessfully")
    memory5 = 0
    print("set memory5 to 0 sucessfully")
    memory6 = 0
    print("set memory6 to 0 sucessfully")
    memory7 = 0
    print("set memory7 to 0 sucessfully")
    memory8 = 0
    print("set memory8 to 0 sucessfully")
    memory9 = 0
    print("set memory9 to 0 sucessfully")
    memory10 = 0
    print("set memory10 to 0 sucessfully")
    memory11 = 0
    print("set memory11 to 0 sucessfully")
    memory12 = 0
    print("set memory12 to 0 sucessfully")
    memory13 = 0
    print("set memory13 to 0 sucessfully")
    memory14 = 0
    print("set memory14 to 0 sucessfully")
    memory15 = 0
    print("set memory15 to 0 sucessfully")
    memory16 = 0
    print("set memory16 to 0 sucessfully")
    memory17 = 0
    print("set memory17 to 0 sucessfully")
    memory18 = 0
    print("set memory18 to 0 sucessfully")
    memory19 = 0
    print("set memory19 to 0 sucessfully")
    memory20 = 0
    print("set memory20 to 0 sucessfully")

    memory1=input("1.boot into MOS1 2.credits 3.bios")
    if memory1 == "1" :
        print("1.calculator")
        print("2.notes")
        print("3.restart")
        memory2=input(" ")
        if memory2 == "1" :
            print("1.+")
            print("2.-")
            print("3.*")
            print("4./")
            memory3=input(" ")
            if memory3 == "1":
                memory4=float(input("enter 1. number "))
                memory5=float(input("enter 2. number "))
                memory6 = memory4 + memory5
                print(memory6)
            elif memory3 == "2":
                memory4=float(input("enter 1. number "))
                memory5=float(input("enter 2. number "))
                memory6 = memory4 - memory5
                print(memory6)
            elif memory3 == "3":
                memory4=float(input("enter 1. number "))
                memory5=float(input("enter 2. number "))
                memory6 = memory4 * memory5
                print(memory6)
            elif memory3 == "4":
                    memory4 = float(input("enter 1. number "))
                    memory5 = float(input("enter 2. number "))
                    memory6 = memory4 / memory5
                    print(memory6)

            else :
                print("wrong selection!")

import os
import random

def boot():
    os.system('clear')
    print("#####[PyBoot 0.1]#####")
    print()
    print("[1] Boot PyOS")
    print("[2] Exit")
    print()
    bo = input()
    if bo == "1" :
        os.system('clear')
        oper()
    elif bo == "2" :
        exit
    else:
        boot()

def oper():
    global dirt
    dirt = "/"
    print ()
    cmd = input("> ")
    if cmd == "run" :
        cmdrun()
    elif cmd == "ls" :
        cmdls()
    elif cmd == "clear" :
        os.system('clear')
        oper()
    elif cmd == "quit" :
        exit
    else:
        print("Command " + cmd + " doesn't exist")
        oper()

def cmdrun():
    app = input("Program:> ")
    if app == "calculator" :
        appcalc()
    elif app == "guess" :
        appguess()
    else:
        print("Program " + app + " not present")
        cmdrun

def appcalc():
    os.system('clear')
    print(" _ _ _ ")
    print()
    sym1 = input("Number 1 > ")
    os.system('clear')
    print(" " + sym1 + " _ _ ")
    print()
    sym2 = input("Symbol [+,-,*,/] > ")
    os.system('clear')
    print(" " + sym1 + " " + sym2 + " _ ")
    print()
    sym3 = input("Number 2 > ")
    os.system('clear')
    print(" " + sym1 + " " + sym2 + " " + sym3 + " ")
    print()
    if sym2 == "+" :
        ans = int(sym1) + int(sym3)
        print(ans)
    elif sym2 == "-" :
        ans = int(sym1) - int(sym3)
        print(ans)
    elif sym2 == "*" :
        ans = int(sym1) * int(sym3)
        print(ans)
    elif sym2 == "/" :
        ans = int(sym1) / int(sym3)
        print(ans)
    else:
        appcalc()
    oper()

def appguess():
    os.system('clear')
    print("Number Guesser")
    print()
    highnum = input("Put in the number cap, lowest is already 1 :> ")
    ranum = random.randint(1,int(highnum))
    os.system('clear')
    print("Number Guesser")
    print()
    rans = int(input("Your random number guess :> "))
    if rans == ranum :
        os.system('clear')
        print("Number Guesser")
        print()
        print("YOU ARE CORRECT!!!")
        ans = input("Do you want to play another round? [y/n]")
        if ans == "y" :
            appguess()
        elif ans == "n" :
            oper()
        else :
            appguess()
    else:
        os.system('clear')
        print("Number Guesser")
        print()
        print("You are wrong! The number was " + str(ranum) + "!")
        print()
        ans = input("Do you want to play again? [y/n] ")
        if ans == "y" :
            appguess()
        else :
            oper()

boot()

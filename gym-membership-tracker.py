from member import member
from payment import payment
from summary import summary
from exit import exit

def mainmenu():
    print("")
    print("====================================")
    print("       GYM MEMBERSHIP SYSTEM        ")
    print("====================================")
    print("")
    print("1) Member Management")
    print("2) Payment Management")
    print("3) Summary")
    print("4) Exit")
    print("")
def main():
    while True:
        mainmenu()
        n = input("Choose Option: ")

        if n == "1":
            member()
        elif n == "2":
            payment()
        elif n == "3":
            summary()
        elif n == "4":
            exit()
            break
        else:
            print("Read the menu carefully and choose accordingly.")
        print("")


if __name__ == "__main__":
    main()

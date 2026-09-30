members = []



def member():
    print("")
    print("====================================")
    print("      MEMBER MANAGEMENT SYSTEM      ")
    print("====================================")
    print("")

    # takc base input of name age
    def addmem():
        name = input("Enter member name: ")
        if name == "":
            print("no name entered, try again")
            return
    
        age = input("Enter age: ")
        if not age.isdigit():
            print("Enter age in digits")
            return
        age = int(age)

        # to chose the plannn
        def plan():
            print("")
            print("=========choose your plan===========")
            print("1) monthly plan")
            print("2) 3 month plan")
            print("3) 6 month plan")
            print("4) 10 month plan")
            print("5) yearly plan")
            print("")

            iputplan = input("Plan you want enroll: ")
            if not iputplan.isdigit():
                print("Your option is invalid")
                return None
            iputplan = int(iputplan)

            if iputplan == 1:
                dura = 1

            elif iputplan == 2:
                dura = 3


            elif iputplan == 3:
                dura = 6

            elif iputplan == 4:
                dura = 10

            elif iputplan == 5:
                dura = 12

            else:
                print("Your option is invalid")
                return None
            return dura

        dura = plan()

        if dura is not None:
            members.append([name, age, dura])
            print("Member added successfully")

    addmem()


            

from member import members


def payment():
    name = input("Enter the member name: ")

    for m in members:
        if m[0] == name:
            dura = m[2]

            if dura == 1:
                fee = 800
            elif dura == 3:
                fee = 2200
            elif dura == 6:
                fee = 4000
            elif dura == 10:
                fee = 6000
            elif dura == 12:
                fee = 7000
            else:
                print("something went wrong")
                return

            print("")
            print("Member name: ", m[0])
            print("Duration: ", dura)
            print("Fee: ", fee)
            return
    print("Member not found")

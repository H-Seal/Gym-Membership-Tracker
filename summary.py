from member import members
from payment import payment


def summary():
    print("======================================")
    print("=============GYM SUMMARY==============")
    print("======================================")
    print("No. of members in Gym: ", len(members))
    print("**************************************")
    for m in members:
        print("member name: ", m[0])
        print("Age: ", m[1])
        print("Duration:", m[2], "months")
        print("")

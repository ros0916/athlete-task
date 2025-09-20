WRM = 9.58
ERM = 9.86
BRM = 9.97

WRF = 10.49
ERF = 10.73
BRF = 10.99

more = 1
def race():
    time = input("What time did the athlete take to complete the race in seconds?\n")
    athlete = input("What gender was the athelete?\n")
    athlete = athlete.lower()
    time = float(time)

    if athlete == "male" or athlete == "man":
        if time < WRM:
            beaten = WRM - time
            print(f"Congratulations! They have beaten the global record by {beaten} seconds.")
            return
        elif time < ERM:
            beaten = ERM - time
            print(f"Congratulations! They have beaten the european record by {beaten} seconds.")
            return
        elif time < BRM:
            beaten = BRM - time
            print(f"Congratulations! They have beaten the british record by {beaten} seconds.")
            return
        else:
            print("Better luck next time.")
    elif athlete == "female" or athlete == "woman":
        if time < WRF:
            beaten = WRF - time
            print(f"Congratulations! They have beaten the global record by {beaten} seconds.")
            return
        elif time < ERF:
            beaten = ERF - time
            print(f"Congratulations! They have beaten the european record by {beaten} seconds.")
            return
        elif time < BRF:
            beaten = BRF - time
            print(f"Congratulations! They have beaten the british record by {beaten} seconds.")
            return
        else:
            print("Better luck next time")

race()
while more == 1:
    ans = input("Would you like to add another athlete?\n")
    if ans.lower() == "yes":
        race()
    elif ans.lower() == "no":
        more = more - 1

print("Thank you for using the race calculator.")


def pressPower():
    print("Power Button Pressed, your brewing machine is on")

def addWater(waterin, capsulein):
    if waterin == True:
        print("machine already has water")
    else:
        if capsulein == True: 
            print("Capsule and water in. Ready to brew")
        elif capsulein == False:
            print("Water in. Insert capsule to brew")
    waterin = True
    return waterin


def insertCapsule(waterin, capsulein):
    if waterin == True:
        print("Capsule and water in. Ready to brew")
    if waterin == False:
        print("Capsule in. Add water to brew")
    capsulein = True


def pressBrew(waterin, capsulein):
    if waterin and capsulein:
        print("Water=1/Capsule=1, action = pressBrew, Final State: )
        print("brewing in progress")
        wait30()
    elif waterin and not capsulein:
        print("insert capsule first")
    elif capsulein and not waterin:
        print("add water first")

def wait30():
    print("you are waiting for the brewing to finish")

def wait300():
    print("300 second time (5min) to turn off coffee maker")


def main():
    waterin = False
    capsulein = False
    pressPower()

    while not waterin and not capsulein:
        action1 = input("what do you want to do? Press 1 to add water, press 2 to insert capsule\n")
        if action1 == '1':
            addWater(waterin, capsulein)
        elif action1 == '2':
            insertCapsule(waterin, capsulein)
        # action2 = input("what do you want to do? Press 1 to add water, press 2 to insert capsule\n")
        # if action2 == '1':
        #     addWater(waterin, capsulein)
        # elif action2 == '2':
        #     insertCapsule(waterin, capsulein)
    
    startBrew = input("type 'brew' to brew...\n")
    
    if startBrew == 'brew':
        pressBrew(waterin, capsulein)
    else:
        print("I am sorry.. that is not a proper request")

    wait30()
    wait300()

if __name__ == "__main__":
    main()

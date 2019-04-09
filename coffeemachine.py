
def pressPower(powerOn):
    print("Power Button Pressed")
    if powerOn:
        print("Machine has been turned OFF")
        powerOn = False
    else: 
        print("Machine has been turned ON")
        powerOn = True
    return powerOn
    
    

def addWater(waterin, capsulein, powerOn):
    if powerOn:
        if waterin == True:
            print("machine already has water")
        else:
            if capsulein == True: 
                print("Adding water...Capsule and water in. Ready to brew")
            elif capsulein == False:
                print("Adding water...Water in. Insert capsule to brew")
    else:
        print("--doing nothing because power is off--\n")
    waterin = True
    return waterin


def insertCapsule(waterin, capsulein, powerOn):
    if powerOn:
        if capsulein == True:
            print("machine already has a capsule in")
        else:
            if waterin == True: 
                print("Adding capsule...Capsule and water in. Ready to brew")
            elif capsulein == False:
                print("Adding Capsule...Capsule in. Add water to brew")
    else:
        print("--doing nothing because power is off--\n")
    waterin = True
    return waterin


def pressBrew(waterin, capsulein, powerOn):
    if powerOn:    
        if waterin and capsulein:
            print("brewing in progress")
        elif waterin:
            print("insert capsule first")
        elif capsulein:
            print("add water first")
        else:
            print("insert capsule and add water before brewing")
    else:
        print("--doing nothing because power is off--\n")

def wait30():
    print("you are waiting for the brewing to finish")

def wait300():
    print("300 second time (5min) to turn off coffee maker")


def main():
    waterin = False
    capsulein = False
    powerOn = False
    
    # while not waterin and not capsulein:
    while True:
        action1 = input("what do you want to do? Enter 'water' to add water, 'capsule' to add coffee capsule, 'power' to press power button or 'brew' to press brew button\n")
        if action1 == 'water':
            waterin = addWater(waterin, capsulein, powerOn)
        elif action1 == 'capsule':
            capsulein = insertCapsule(waterin, capsulein, powerOn)
        elif action1 == 'power':
            powerOn = pressPower(powerOn)
        elif action1 == 'brew':
            pressBrew(waterin, capsulein, powerOn)
        else:
            print("I am sorry.. that is not a proper request")

    wait30()
    wait300()

if __name__ == "__main__":
    main()

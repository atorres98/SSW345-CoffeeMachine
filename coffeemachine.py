def pressPower(powerOn):
    print("Power Button Pressed")
    if powerOn:
        print("Machine has been turned OFF\n")
        powerOn = False
    else: 
        print("Machine has been turned ON\n")
        powerOn = True
    return powerOn
    
    

def addWater(waterin, capsulein, powerOn):
    if waterin == True:
        print("machine already has water\n")
    else:
        if capsulein == True: 
            print("Adding water...Capsule and water in. Ready to brew\n")
        elif capsulein == False:
            print("Adding water...Water in. Insert capsule to brew\n")
    waterin = True
    return waterin


def insertCapsule(waterin, capsulein, powerOn):
    if capsulein == True:
        print("machine already has a capsule in\n")
    else:
        if waterin == True: 
            print("Adding capsule...Capsule and water in. Ready to brew\n")
        elif capsulein == False:
            print("Adding Capsule...Capsule in. Add water to brew\n")
    waterin = True
    return waterin


def pressBrew(waterin, capsulein, powerOn):
    if powerOn:    
        if waterin and capsulein:
            print("brewing in progress \n . \n . \n . \n . \n ")
            wait30()
            print("Cup is ready\n")
            wait300()
        elif waterin:
            print("insert capsule first\n")
        elif capsulein:
            print("add water first\n")
        else:
            print("insert capsule and add water before brewing\n")
    else:
        print("--doing nothing because power is off--\n")

def wait30():
    print("...you are waiting 30s for the brewing to finish\n")

def wait300():
    print("...300 second time (5min) to turn off coffee maker\n")


def main():
    waterin = False
    capsulein = False
    powerOn = False
    
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

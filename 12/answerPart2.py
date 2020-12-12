with open('input', newline='\r\n') as inputfile:
    input=inputfile.read().split('\r\n')

directions=['E','N','W','S']

upDown=0
leftRight=0
currentDirection='E'
multiplier=1
waypoint=(1,10)
for entry in input:
    # print(currentDirection," ", upDown, " ", leftRight)
    # print(waypoint)
    action=entry[0]
    number=int(entry[1:])
    if(action=="N"):
        waypoint=(waypoint[0]+number,waypoint[1])
    elif (action == "S"):
        waypoint=(waypoint[0]-number,waypoint[1])
    elif (action == "E"):
        waypoint=(waypoint[0],waypoint[1]+number)
    elif (action == "W"):
        waypoint=(waypoint[0],waypoint[1]-number)
    elif(action=="F"):
        upDown=upDown+number*waypoint[0]
        leftRight=leftRight+number*waypoint[1]
    elif(action=="L"):
        dirChange=int(number/90)
        if(dirChange%4==1):
            waypoint = ( waypoint[1], -1*waypoint[0])
        elif (dirChange % 4 == 2):
            waypoint=(-1*waypoint[0],-1*waypoint[1])
        elif (dirChange % 4 == 3):
            waypoint = (-1*waypoint[1], waypoint[0])
    elif(action=="R"):
        dirChange = int(number / 90)
        if (dirChange % 4 == 1):
            waypoint = (-1*waypoint[1], waypoint[0])
        elif (dirChange % 4 == 2):
            waypoint = (-1 * waypoint[0], -1 * waypoint[1])
        elif (dirChange % 4 == 3):
            waypoint = ( waypoint[1], -1*waypoint[0])
print(currentDirection," ", upDown, " ", leftRight)
print(abs(upDown)+abs(leftRight))


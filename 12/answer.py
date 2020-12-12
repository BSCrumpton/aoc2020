with open('input', newline='\r\n') as inputfile:
    input=inputfile.read().split('\r\n')

directions=['E','N','W','S']

upDown=0
leftRight=0
currentDirection='E'
multiplier=1
for entry in input:
    # print(currentDirection," ", upDown, " ", leftRight)
    action=entry[0]
    number=int(entry[1:])
    if(action=="N"):
        upDown=upDown+number
    elif (action == "S"):
        upDown = upDown - number
    elif (action == "E"):
        leftRight = leftRight + number
    elif (action == "W"):
        leftRight = leftRight - number
    elif(action=="F"):
        if(currentDirection=="E" or currentDirection=="W"):
            leftRight=leftRight + number*multiplier
        if (currentDirection == "N" or currentDirection == "S"):
            upDown = upDown + number * multiplier
    elif(action=="L"):
        dirChange=int(number/90)
        index=directions.index(currentDirection)
        currentDirection=directions[(index+dirChange)%len(directions)]
        if (currentDirection == "S" or currentDirection == "W"):
            multiplier = -1
        else:
            multiplier = 1
    elif(action=="R"):
        dirChange = int(number / 90)
        index = directions.index(currentDirection)
        currentDirection = directions[index - dirChange%len(directions)]
        if(currentDirection=="S" or currentDirection=="W"):
            multiplier=-1
        else:
            multiplier=1
# print(currentDirection," ", upDown, " ", leftRight)
print(abs(upDown)+abs(leftRight))


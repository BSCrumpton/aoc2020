import copy
with open('input', newline='\r\n') as inputfile:
    input=inputfile.read().split('\r\n')

input = [list(i) for i in input]

adjacency=[(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

def printMap(input):
    for row in input:
        print(row)
    print()
# printMap(input)


def shouldSwap(row,column,map):
    type=map[row][column]
    countFilled=0
    for seat in adjacency:
        seatRow=row+seat[0]
        seatColumn=column+seat[1]
        if(seatRow<0 or seatColumn<0 ):
            continue
        try:
            seatType=map[seatRow][seatColumn]
            while(seatType=="."):
                seatRow = seatRow + seat[0]
                seatColumn = seatColumn + seat[1]
                if (seatRow < 0 or seatColumn < 0):
                    seatType=""
                else:
                    seatType = map[seatRow][seatColumn]
            # if(row==78 and column==0):
            #     print(seatRow,' ', seatColumn, ' ',map[seatRow][seatColumn])
            if(seatType=="#"):
                countFilled=countFilled+1
        except Exception as e:
            # print(e)
            continue
    if(type=="L" and countFilled==0):
        return True
    elif(type=="#" and countFilled>4):
        return True
    else:
        return False

for i in range(170):
    tempMap=copy.deepcopy(input)
    for rowindex,row in enumerate(input):
        for slotindex,slot in enumerate(row):
            # printMap(input)
            if(shouldSwap(rowindex,slotindex,input)):
                if(input[rowindex][slotindex]=="L"):
                    tempMap[rowindex][slotindex] = "#"
                else:
                    tempMap[rowindex][slotindex] = "L"
        # break
    input=copy.deepcopy(tempMap)


printMap(input)

filledCount=0
for row in input:
    for column in row:
        if(column=="#"):
            filledCount=filledCount+1
print(filledCount)

#not 2003
# not 2236
# not 703
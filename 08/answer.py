with open('input', newline='\r\n') as inputfile:
    input=inputfile.read().split('\r\n')

accumulator=0
ranlines=[]
noOpsAndJmps=[]
for index,row in enumerate(input):
    temp=row.split()[0]
    if(temp=="nop" or temp=="jmp"):
        noOpsAndJmps.append(index)

def doRow(rownumber,accumulator,fixed):
    # print(rownumber, ' ',input[rownumber]," | ",accumulator)
    if(rownumber>len(input)):
        print(accumulator)
        return False
    if (rownumber in ranlines):
        print(accumulator)
        return True
    tokens = input[rownumber].split()
    if rownumber == fixed:
        if(tokens[0]=="nop"):
            tokens[0]="jmp"
        else:
            tokens[0]="nop"
    ranlines.append(rownumber)
    if(tokens[0]=="acc"):
        accumulator=accumulator+int(tokens[1])
        doRow(rownumber + 1, accumulator,fixed)
    elif(tokens[0]=="jmp"):
        doRow(rownumber+int(tokens[1]), accumulator,fixed)
    else:
        doRow(rownumber+1,accumulator,fixed)


doRow(0,0,-1)

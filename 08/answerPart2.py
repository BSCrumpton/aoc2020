with open('input', newline='\r\n') as inputfile:
    input=inputfile.read().split('\r\n')

accumulator=0
noOpsAndJmps=[]
for index,row in enumerate(input):
    temp=row.split()[0]
    if(temp=="nop" or temp=="jmp"):
        noOpsAndJmps.append(index)
# print(noOpsAndJmps)

def doRow(rownumber,accumulator,fixed,ranlines):
    # print(rownumber, ' ',input[rownumber]," | ",accumulator)
    # print("fixed: ",fixed)
    if(rownumber>len(input)-1):
        # print(fixed)
        print(accumulator)
        return False
    if (rownumber in ranlines):
        # print(accumulator)
        return True
    tokens = input[rownumber].split()
    if rownumber == fixed:
        # print(fixed)
        if(tokens[0]=="nop"):
            tokens[0]="jmp"
        else:
            tokens[0]="nop"
    ranlines.append(rownumber)
    if(tokens[0]=="acc"):
        accumulator=accumulator+int(tokens[1])
        return doRow(rownumber + 1, accumulator,fixed,ranlines)
    elif(tokens[0]=="jmp"):
        return doRow(rownumber+int(tokens[1]), accumulator,fixed,ranlines)
    else:
        return doRow(rownumber+1,accumulator,fixed,ranlines)


inLoop=True

while (inLoop):
    # inLoop=doRow(0,0,-1)
    # print(inLoop)
    ranlines=[]
    if(inLoop):
        inLoop=doRow(0,0,noOpsAndJmps[0],ranlines)
    if(inLoop):
        # print("didn't solve")
        noOpsAndJmps=noOpsAndJmps[1:]
        # print(noOpsAndJmps)
    else:
        break
# 432 not correct
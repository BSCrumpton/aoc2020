with open('input', newline='\r\n') as inputfile:
    input=inputfile.read().split('\r\n')
for i in input:
    i=int(i)
# print(input)
preamblelen=25
preamble=input[0:preamblelen]

def checkIfSum(numberlist,sum):
    for index,number in enumerate(numberlist):
        for number2 in numberlist[(index+1):]:
            # if(sum==422):
                 # print(number, " ",number2,' ',int(number)+int(number2))
            if((int(number)+int(number2))==sum):
                return False
    print(sum)
    return True

result=False
index=1
while (not result):
    tempSum=(int(input[index+preamblelen]))
    # print(preamble)
    result=checkIfSum(preamble,tempSum)
    preamble=input[index:preamblelen+index+1]
    index=index+1

# not 422
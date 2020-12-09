with open('input', newline='\r\n') as inputfile:
    input=inputfile.read().split('\r\n')
for i in input:
    i=int(i)
input = [int(i) for i in input]
# print(input)
# preamblelen=25
# preamble=input[0:preamblelen]
#
#
#
# def checkIfSum(numberlist,sum):
#     for index,number in enumerate(numberlist):
#         for number2 in numberlist[(index+1):]:
#             # if(sum==422):
#                  # print(number, " ",number2,' ',int(number)+int(number2))
#             if((int(number)+int(number2))==sum):
#                 return False
#     print(sum)
#     return True
#
# result=False
# index=1
# while (not result):
#     tempSum=(int(input[index+preamblelen]))
#     # print(preamble)
#     result=checkIfSum(preamble,tempSum)
#     preamble=input[index:preamblelen+index+1]
#     index=index+1
# # not 422

tempSum=int(1930745883)
print(tempSum)
result=True
index=0
while(result):
    localVar=0
    # print(index)
    for resultindex,number in enumerate(input[index+1:]):
        # print(resultindex," ", number)
        localVar=localVar+int(number)
        if(localVar>tempSum):
            index=index+1
            localVar=0
            break
        if(localVar==tempSum):
            print(localVar)
            result=False
            print(input[index:index+resultindex+2])
            print(sum(input[index+1:index+resultindex+2]))
            print(min(input[index+1:index+resultindex+2])+max(input[index+1:resultindex+index+2]))
    index=index+1
    if(index>1000):
        result=False

# not 241325574
with open('input', newline='\r\n') as inputfile:
    input=inputfile.read().split('\r\n')

input = [int(i) for i in input]
# print(input)
input.sort()
print(input)
input.insert(0,0)
resultList=[]

problemNumbers=[]

def recurCheckPath(resultList,tempResultList,index):
    if(input[index]in problemNumbers):
        return
    newtempResultList=tempResultList.copy()
    newtempResultList.append(input[index])
    if(index==len(input)-1):
        resultList.append(newtempResultList)
        return
    didOne=False
    for i in range(1,10):
        try:
            difference=input[index + i] - input[index]
        except Exception as e:
            # print(e)
            # newtempResultList.append(input[index])
            # resultList.append(newtempResultList)
            return
        # print(input[index+i],' ',input[index],' ',difference)
        if(difference<4):
            didOne=True
            recurCheckPath(resultList,newtempResultList,index+i)
        else:
            # problemNumbers.append(input[index])
            # resultList.append(newtempResultList)
            break
    if(not didOne):
        problemNumbers.append(input[index])
recurCheckPath(resultList,[],0)
print("finished gathering potentials")
unique_data = [list(x) for x in set(tuple(x) for x in resultList)]

print(len(resultList))
# print(resultList)

# not 3
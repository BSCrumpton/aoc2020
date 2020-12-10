with open('input', newline='\r\n') as inputfile:
    input=inputfile.read().split('\r\n')

input = [int(i) for i in input]
# print(input)
input.sort()
# print(input)
oneDiff=0
twoDiff=0
threeDiff=0
for index,adapter in enumerate(input):
    try:
        # print(index,' ',input[index],' ',input[index-1])
        if(index==0):
            difference=input[index]
        else:
            difference=input[index]-input[index-1]
        # print(difference)
        if(difference>3):
            break
        if(difference==1):
            oneDiff=oneDiff+1
        if (difference == 2):
            twoDiff = twoDiff + 1
        if (difference == 3):
            threeDiff = threeDiff + 1
    except Exception as e:
        difference=input[index]
        if (difference > 3):
            break
        if (difference == 1):
            oneDiff = oneDiff + 1
        if (difference == 2):
            twoDiff = twoDiff + 1
        if (difference == 3):
            threeDiff = threeDiff + 1
        print(e)
        break
threeDiff=threeDiff+1
print(oneDiff,' ',threeDiff)
print(oneDiff*threeDiff)
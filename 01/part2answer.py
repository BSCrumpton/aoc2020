import csv

input = []
with open('input', newline='') as inputfile:
    for row in csv.reader(inputfile):
        input.append(int(row[0]))
for idx,number in enumerate(input):
    templist=input[idx:]
    for idx2,number2 in enumerate(templist):
        anothertemplist=input[idx2:]
        for number3 in anothertemplist:
            if(number+number2+number3==2020):
                print(number*number2*number3)
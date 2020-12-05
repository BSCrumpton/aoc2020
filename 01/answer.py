import csv

input = []
with open('input', newline='') as inputfile:
    for row in csv.reader(inputfile):
        input.append(int(row[0]))
tried = []
for idx,number in enumerate(input):
    if(number in tried):
        continue
    templist=input[idx:]
    for number2 in templist:
        if(number+number2==2020):
            print(number*number2)
    tried.append(number)
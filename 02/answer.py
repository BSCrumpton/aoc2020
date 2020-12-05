import csv

input = []
with open('input', newline='') as inputfile:
    for row in csv.reader(inputfile):
        input.append(row[0])
correctCount=0
for line in input:
    tokens=line.split(" ")
    min=int(tokens[0].split("-")[0])
    max = int(tokens[0].split("-")[1])
    necessaryletter=tokens[1][0]
    string=tokens[2]
    letterCount=0
    for letter in string:
        if letter is necessaryletter:
            letterCount=letterCount+1
    if (letterCount >= min and letterCount <= max):
        correctCount=correctCount+1
print(correctCount)
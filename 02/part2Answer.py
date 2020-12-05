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
    try:
        if ((string[min-1]==necessaryletter) ^ (string[max-1]==necessaryletter)):
            correctCount=correctCount+1
    except Exception:
        if(string[min-1]==necessaryletter):
            correctCount = correctCount + 1
print(correctCount)
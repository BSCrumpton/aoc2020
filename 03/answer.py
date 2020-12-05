import csv

map = []
with open('input', newline='') as inputfile:
    for row in csv.reader(inputfile):
        splitrow=[]
        for letter in row[0]:
            splitrow.append(letter)
        map.append(splitrow)
rise=2
run=1
# 1,3 is 211
# 1,1 is 67
# 5,1 is 77
# 7,1 is 89
# 1,2 is 37
# part 2 is 3584591857

collisions=0
x=0
y=0
while(True):
    try:
        if(map[y][x]=="#"):
            collisions=collisions+1
        x=x+run
        y=y+rise
    except IndexError:
        if(y<len(map)-1):
            x=x-len(map[0])
            continue
        print(collisions)
        exit(0)
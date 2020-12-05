with open('input', newline='\r\n') as inputfile:
    input=inputfile.read().split('\r\n')
IDs=[]

def getRow(string):
    rows=list(range(128))
    for letter in string:
        if(letter=='F'):
            rows=rows[0:len(rows)//2]
        if(letter=='B'):
            rows = rows[len(rows) // 2:]
    return rows[0]
def getColumn(string):
    columns = list(range(8))
    for letter in string:
        if (letter == 'L'):
            columns = columns[0:len(columns) // 2]
        if (letter == 'R'):
            columns = columns[len(columns) // 2:]
    return columns[0]

def getID(boardingPass):
    return getRow(boardingPass[:-3])*8+getColumn(boardingPass[-3:])

ids=[]
for boardingPass in input:
    id=getID(boardingPass)
    ids.append(id)
for seat in ids:
    if (seat+1 not in ids or seat-1 not in ids):
        print(seat)
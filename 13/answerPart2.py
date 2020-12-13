with open('input', newline='\r\n') as inputfile:
    input=inputfile.read().split('\r\n')

departureTime=int(input[0])
busIds=input[1].split(",")
busIds = [int(i) for i in busIds if i!="x"]

cantGo=True
i=0
goId=0
while(cantGo):
    for id in busIds:
        if((departureTime+i)%id==0):
            cantGo=False
            goId=id
    i=i+1
print(goId," ",i-1)
print(goId*(i-1))

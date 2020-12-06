with open('input', newline='\r\n') as inputfile:
    input=inputfile.read()
entries=input.split("\r\n\r\n")
sum=0
for entry in entries:
    temp={}
    linecount=1
    for letter in entry:
        if(letter=="\n"):
            linecount=linecount+1
    # print(linecount)
    entry=entry.replace("\n",'')
    entry = entry.replace("\r", '')

    for letter in entry:
        temp[letter]=temp.get(letter,0)+1
    # print(temp)
    for key,value in temp.items():
        if(value==linecount):
            sum=sum+1
    # break
    # sum=sum+len(temp)
print(sum)
# 407 not right
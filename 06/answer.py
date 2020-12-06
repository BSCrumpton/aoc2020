with open('input', newline='\r\n') as inputfile:
    input=inputfile.read()
entries=input.split("\r\n\r\n")
sum=0
for entry in entries:
    temp={}
    entry=entry.replace("\n",'')
    entry = entry.replace("\r", '')
    for letter in entry:
        temp[letter]=0
    print(temp)
    # break
    sum=sum+len(temp)
print(sum)
# 6761 not right
with open('input', newline='\r\n') as inputfile:
    input=inputfile.read().split('\r\n')
contains={}
containsGold={}
baseBags=[]
for rule in input:
    tokens=rule.split()
    location=1
    temp={}
    for index,word in enumerate(tokens):
        word=word.strip()
        # print(index,' ',word)
        if(word=="bags," or word=="bag," or word=="bag." or word=="bags."):
            if(index==2):
                continue
            if(tokens[index-2]=="no"):
                baseBags.append(tokens[0]+" "+tokens[1])
                continue
            temp[tokens[index-2]+" "+tokens[index-1]]=tokens[index-3]
    if(not temp):
        continue
    contains[tokens[0]+" "+tokens[1]]=temp
# print (baseBags)
# print(contains)
# print(contains)
#
while (len(containsGold)!=len(input)):
    # print(len(containsGold), ' ',len(contains))
    for key,value in contains.items():
        # print(key, " ", value)
        for innerkey,innervalue in value.items():
            if innerkey=="shiny gold":
                # print(key, value)
                # print(innerkey, innervalue)
                # print(containsGold[key])
                containsGold[key]=int(innervalue)
                # print(key, containsGold[key])
                continue
            if(innerkey in containsGold):
                containsGold[key] = int(containsGold[innerkey])+containsGold.get(key,0)
                continue
            if(innerkey in baseBags):
                containsGold[innerkey]=0
    # print(containsGold)
    # break
def runMore():
    for key,value in contains.items():
        # print(key, " ", value)
        for innerkey,innervalue in value.items():
            if innerkey=="shiny gold":
                # print(key, value)
                # print(innerkey, innervalue)
                # print(containsGold[key])
                containsGold[key]=int(innervalue)
                # print(key, containsGold[key])
                continue
            if(innerkey in containsGold):
                containsGold[key] = int(containsGold[innerkey])+containsGold.get(key,0)
                continue
            if(innerkey in baseBags):
                containsGold[innerkey]=0

runMore()
runMore()
runMore()
runMore()
runMore()
runMore()
runMore()
runMore()
runMore()
runMore()
runMore()
runMore()
runMore()
runMore()
runMore()
runMore()
runMore()
runMore()
runMore()
runMore()
runMore()
runMore()
runMore()

# print("eventually made it")
count=0
for key,value in containsGold.items():
    # print(key, " ", value)
    if(value >0):
        count=count+1
print(count)
# not 121, too low
# not 213, too low
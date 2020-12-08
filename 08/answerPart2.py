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
            temp[tokens[index-2]+" "+tokens[index-1]]=int(tokens[index-3])
    if(not temp):
        continue
    contains[tokens[0]+" "+tokens[1]]=temp
# print (baseBags)
# print(contains)
# print(contains)
#
def recurGetBags(bagType):

    tempContainedBags=0
    if(bagType in baseBags):
        return 0
    # print(bagType)
    # print(bagType,' ',contains[bagType])
    for recurkey, recurvalue in contains[bagType].items():
        temp=recurGetBags(recurkey)
        # print(bagType,' ' ,temp,'*',recurvalue)
        temp=temp+1
        tempContainedBags = tempContainedBags + (recurvalue * temp )
    # print(tempContainedBags)
    return tempContainedBags


containedBags=0
for key,value in contains["shiny gold"].items():
    # print(key,' ',value)
    containedBags=containedBags+(value*recurGetBags(key))+value
    # print(containedBags)
    # break


# print(containsGold)
# break}
print(containedBags)
# 145043 too low
# 145057 not correct
# 202270 not correct
172246
with open('input', newline='\r\n') as inputfile:
    input=inputfile.read()
entries=input.split("\r\n\r\n")

entries[:] = [entry.replace("\r\n",' ') for entry in entries]

required=['byr','iyr','eyr','hgt','hcl','ecl','pid']

def isValid(passport):
    tokens=passport.split(" ")
    has=[]
    for line in tokens:
        has.append(line.split(":")[0])
    for element in required:
        if(element in has):
            continue
        else:
            return False
    return True


validCount=0
for entry in entries:
    if(isValid(entry)):
        validCount=validCount+1
print(validCount)

# 279 not correct
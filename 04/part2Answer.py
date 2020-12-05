with open('input', newline='\r\n') as inputfile:
    input=inputfile.read()
entries=input.split("\r\n\r\n")

entries[:] = [entry.replace("\r\n",' ') for entry in entries]

required=['byr','iyr','eyr','hgt','hcl','ecl','pid']

allowedEcl=['amb','blu','brn','gry','grn','hzl','oth']

allowedDigits=['a','b','c','d','e','f','0','1','2','3','4','5','6','7','8','9']

def validateData(key,entry):
    # print(key,'\n',entry)
    if(key=='byr'):
        if(int(entry)>=1920 and int(entry)<=2002 and len(entry)<6):
            return True
    elif(key=='iyr'):
        if (int(entry) >= 2010 and int(entry) <= 2020 and len(entry) <6):
            return True
    elif(key=='eyr'):
        if (int(entry) >= 2020 and int(entry) <= 2030 and len(entry) <6):
            return True
    elif(key=='hgt'):
        if(entry.find('i')!=-1):
            hgt=int(entry.split('i')[0])
            if(hgt>=59 and hgt <=76):
                return True
        elif(entry.find('c')!=-1):
            hgt=int(entry.split('c')[0])
            if (hgt >= 150 and hgt <= 193):
                return True
    elif(key=='hcl'):
        if(entry[0]=='#'):
            for digit in entry[1:]:
                if(digit in allowedDigits):
                    continue
                else:
                    return False
            return True
    elif(key=='ecl'):
        if(entry in allowedEcl):
            return True
    elif(key=='pid'):
        if(len(entry)==9):
            return True
    return False

def isValid(passport):
    tokens=passport.split(" ")
    has={}
    for line in tokens:
        has[line.split(":")[0]]=line.split(":")[1]
    for element in required:
        if(element in has):
            if(validateData(element,has[element])):
                continue
            else:
                return False
        else:
            return False
    return True


validCount=0
for entry in entries:
    if(isValid(entry)):
        validCount=validCount+1

print(validCount)

# 279 not correct
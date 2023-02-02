# count how many "C" and how many "I" in the string

def count(string):
    countC = 0
    countI = 0
    for i in string:
        if i == "C" or i == "c":
            countC += 1
        elif i == "I" or i == "i":
            countI += 1
    return countC, countI

str =  "cCICCICiiciiciiciiicii"
print(count(str))
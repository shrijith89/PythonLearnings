str1 = "ThIsisCoNfUsInG"
f = "is"
newStr = ""
count = 0

for i in range(0, len(str1)-len(f)+1):
    newStr = ""
    for j in range(i, i+len(f)):
        newStr += str1[j]
    if newStr == f:
        count += 1

print(count)
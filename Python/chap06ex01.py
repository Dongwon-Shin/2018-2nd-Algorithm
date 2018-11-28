strInput = "aaabbcccccca"
curChar = ""
prev = strInput[0]
count = 0
for i in strInput:
    if i == prev:
        count += 1
    else:
        curChar += prev + str(count)
        count = 1
    prev = i
curChar += prev + str(count)
print(curChar)
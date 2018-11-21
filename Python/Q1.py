strInput = "aaabbcccccca"

curChar = "" #초기값 설정
count = 0 #문자 수 카운팅

for i in strInput:
    if curChar == i:  
        count = count + 1
    else:
        print(curChar, i)
        count = 1 
    curChar = i

print(curChar, i)
s = "aaabbcccccca"
r = ""
prev = s[0]
cnt=0
for c in s:
    if c == prev:
        cnt += 1
    else:
        r += prev + str(cnt)
        cnt=1
    prev = c
r += prev + str(cnt)
print(r)
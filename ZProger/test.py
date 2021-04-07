cnt = 0
for i in range(1000, 10000):
    s = 0
    for j in str(i):
        s += int(j)
    if s == 20:
        cnt += i
print(cnt)
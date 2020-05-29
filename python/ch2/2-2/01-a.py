# 2-2 練習題
i = []
total = 0
for k in range(10):
    i.append(k+1)
    # print(i)
for k in range(10):
    total += i[k]
print("%d" % total)

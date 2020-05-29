arr2 = []
total = 0
for i in range(5):
    new = []
    for j in range (5):
        new.append(i + j)
        print("%3d" % new[j], end = '') # %3d(3為整數, 缺的補空格), end = '' (輸出不換行)
        arr2.append(new)
    print() # 換行
for i in range(5):
    for j in range(5):
        total += arr2[i][j]
        print("total = %d" % total)
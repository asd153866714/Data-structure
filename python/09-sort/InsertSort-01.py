# InsertSort
def InsertSort(data):
    for i in range(1, len(data)):
        print('i: ',i)
        for j in range(i-1, -1, -1):
            print('j: ', j)
            if data[j] > data[j+1]:
                temp = data[j]
                data[j] = data[j+1]
                data[j+1] = temp
            else:
                break
    return data

data = [5, 3, 2, 9]
print(InsertSort(data))

# 有 Bug
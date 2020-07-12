# InsertSort
def InsertSort(data):
    for i in range(1, len(data)):
        j = i - 1
        while data[j] > data[j+1] and j >= 0:
            data[j], data[j+1] = data[j+1], data[j]
            j -= 1
    return data

data = [5, 3, 2, 9]
print(InsertSort(data))
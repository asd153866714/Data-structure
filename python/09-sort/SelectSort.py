# SelectSort
def SelectSort(data):
    for i in range(0, len(data) - 1):
        minIndex = i
        for j in range(i+1, len(data)):
            if data[j] < data[minIndex]:
                minIndex = j
        if minIndex != i:
            data[i], data[minIndex] = data[minIndex], data[i]
    return data

data = [5, 3, 2, 9]
print(SelectSort(data))
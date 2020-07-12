# BubbleSort

def BubbleSort(data):
    for i in range(0, len(data) - 1):
        for j in range(0, len(data) - 1 - i):
            if data[j] > data[j+1]:
                temp = data[j]
                data[j] = data[j+1]
                data[j+1] = temp
    return data
data = [5, 4, 8, 3]
print(BubbleSort(data))
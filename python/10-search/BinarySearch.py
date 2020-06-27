# 二元搜尋

value = 0

def binary_search(data):
    global value

    low = 0
    high = len(data) - 1

    while (low <= high):
        mid = int((low + high)/2)
        if (value == data[mid]):
            print('\nFound %d is the index %d' % (value, mid))
            return mid
        elif (value > data[mid]):
            low = mid + 1
        else :
            high = mid - 1 
    print('\nSorry, %d not found' % value)   
    return -1

def main():
    global value
    data = [1,3,9,11,15,19,29]

    print('Sorted data: ', end = '')
    for i in range(7):
        print(data[i], ' ', end = '')
    print()

    while True:
        value = int(input('\nWhat number do you want to search? '))
        
        print('\nSearching......')
        binary_search(data)

main()
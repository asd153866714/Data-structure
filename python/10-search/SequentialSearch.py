# 循序搜尋

input_ = 0

def search(data):
    global input_

    i = 0
    while i < 10:
        print('#%-2d is %-2d' % (i, data[i]))
        if input_ == data[i]:
            break
        else:
            i += 1
    
    if i == 10:
        print('\nSorry, ', input_, 'not fonud')
    else:
        print('\nFound, ', input_, 'is index ', i, 'record')

def main():
    global input_
    
    data = [35, 75, 23, 44, 57, 12, 29, 64, 38, 82]
    print('\n<< Sequential search >>')
    print('\nData: ', end = '')

    for i in range(10):
        print(data[i], ' ', end = '')
    print()

    while True:
        input_ = int(input('\nWhat number do you want to search? '))
        
        print('\nSearching......')
        search(data)

        ch = input('要繼續搜尋嗎？（y/n）： ')
        if ch == 'n':
            break
main()
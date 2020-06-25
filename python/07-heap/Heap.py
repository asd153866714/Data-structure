# 利用 Heap 處理會員推出資料──新增、刪除、輸出
import sys

MAX = 100
heap_tree = [0] * MAX   # Heap陣列
last_index = 0          # 最後一筆資料的index

# 新增
def insert():
    global MAX
    global last_index

    if last_index >= MAX-1:
        print('\n   Login members are full, more than %d !!' % MAX - 1)
        print('   Please wait ')
    id = int(input('\n   Please enter login ID number: '))
    create(id)  # 建立Heap
    print('     Login successfully!!')

# 刪除 
def delete():
    global last_index

    del_id = 0
    del_index = 0

    if last_index < 1:
        print('\n   Login member is empty')
    else:
        del_id = int(input('\n   Please enter logout ID number: '))
        del_index = search(del_id)

        if del_index == 0:
            print('   ID number not found!!')
        else:
            remove(del_index) # 刪除資料，並調整 Heap
            print('   ID number: ', del_id, ' logout!!')

# 顯示
def display():
    global last_index
    option = ' '

    if last_index < 1:
        print('\n   No member to show!!\n')
    else:
        print()
        print('********************')
        print('   <1> increase') # 選擇第一項為由小到大排列
        print('   <2> decrease') # 選擇第二項為由大到小排列
        print('********************')
        while True:
            try:
                option = input('\n   Please enter your option: ')
            except ValueError:
                print()
                print('Not a correctly number.')
                print('Try again\n')
            if (option == '1' or option == '2'):
                break
        show(option)

# 建立資料於 Heap
def create(id_temp):
    global last_index
    global heap_tree
    
    last_index += 1
    heap_tree[last_index] = id_temp # 將資料新增於最後
    adjust_u(heap_tree, last_index) # 調整新增資料

# 從 Heap 中刪除資料
def remove(del_index):
    global last_index
    global heap_tree
    
    # 以最後一筆資料代替被刪除資料
    heap_tree[del_index] = heap_tree[last_index]
    heap_tree[last_index] = 0
    last_index -= 1
    
    if last_index > 1:  # 當資料筆數大於 1 筆，則做調整

        # 當替代資料大於其PARENT NODE，則往上調整
        if heap_tree[del_index] > heap_tree[del_index // 2] and del_index > 1:
            adjust_u(heap_tree, del_index)

        # 替代資料小於其CHILDREN NODE，則往下調整
        else:
            adjust_d(heap_tree, del_index, last_index-1)

def show(op):
    global last_index
    global heap_tree
    heap_temp = []

    # 將Heap資料複製到另一個陣列作排序工作
    heap_temp = [i for i in heap_tree]

    index_temp = last_index - 1

    # 將陣列調整為由小到大排列
    while index_temp > 0:
        exchange(heap_temp, 1, index_temp + 1)
        adjust_d(heap_temp, 1, index_temp)
        index_temp -= 1

    print('\n\n   ID number')
    print(' **********************') 

    # 選擇第一種方式輸出，以遞迴方式輸出──使用堆疊
    # 選擇第二種方式輸出，以遞迴方式輸出──使用佇列
    if op == '1':
        for index_temp in range(1, last_index + 1):
            print(' ', heap_temp[index_temp])
    elif op == '2':
        index_temp = last_index
        while index_temp > 0:
            print(' ', heap_temp[index_temp])
            index_temp -= 1

    print(' **********************')
    print(' Total member: ', last_index, '\n')

# 向上調整
def adjust_u(heap_tree, index):
    while index > 1:
        if heap_tree[index] <= heap_tree[index // 2]:
            break
        else:
            exchange(heap_tree, index, index // 2)
        index //= 2

# 向下調整，index1 為陣列中要調整的資料，index2 為陣列中最後一筆資料
def adjust_d(heap_tree, index1, index2):

    # id_temp記錄目前資料，index_temp 則是目前資料之 CHILDREN NODE 的 INDEX
    id_temp = heap_tree[index1]
    index_temp = index1 * 2

    # 當比較資料之 INDEX 不大於最後一筆資料之 INDEX，則繼續比較
    while index_temp <= index2:
        if index_temp < index2 and heap_tree[index_temp] < heap_tree[index_temp + 1]:         
            index_temp += 1 # index_temp記錄目前資料之CHILDREN NODE中較大者
        if id_temp >= heap_tree[index_temp]: # 比較完畢則跳出，否則交換資料
            break
        else:
            heap_tree[index_temp // 2] = heap_tree[index_temp]
            index_temp *= 2       
    heap_tree[index_temp // 2] = id_temp

# 交換傳來之 id1 及 id2 儲存之資料
def exchange(arr, id1, id2):
    id_temp = arr[id1]
    arr[id1] = arr[id2]
    arr[id2] = id_temp

# 尋找陣列中 id_temp
def search(id_temp):
    global heap_tree

    for index in  range(1, len(heap_tree)):
        if id_temp == heap_tree[index]:
            return index
    return 0

def main():
    option = ''
    while True:
        print('\n****** HeapTree Program ******')
        print('       <1> Login              ')
        print('       <2> Logout             ')
        print('       <3> Show               ')
        print('       <4> Exit               ')
        print('******************************')
        
        try:
            option = input('      Choice : ')
        except ValueError:
            print('Not a correct number.')
            print('Try again\n')
        
        if option == '1':
            insert()
        elif option == '2':
            delete()
        elif option == '3':
            display()
        elif option == '4':
            sys.exit(0)
        else:
            print('     Invalid option!!')
main()
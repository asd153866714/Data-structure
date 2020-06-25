# 二元搜尋樹的加入、刪除與修改

import sys

class Student:
    name = '' # 學生姓名
    score = 0 # 學生成績
    llink = None # 左子鏈結
    rlink = None # 右子鏈結

root = None

def insert():
    name = " "
    score = 0
    print("\n=====INSERT DATA====='")
    name = input('Enter student name: ')
    score = eval(input('Enter student score: '))

    access(name, score)

def delete():
    global root
    name = " "

    if root == None:
        print('No student record!')
        return
    print('\n=====DELETE DATA=====')
    name = input('Enter student name: ')

    remove(name)

def modify():
    global root
    node = None
    name = " "

    if root == None: # 判斷根節點是否為空
        print('No student record!')
        return
    else:
        print('\n=====MODIFY DATA=====')
        name = input('Enter student name: ')

        node = search(name)
        if node == None:
            print('Student %s not found!' % name)
        else:
            print('Original student name: ', node.name)
            print('Original student score: ', node.score)
            node.score = eval(input('Enter new score: '))
            print('Student %s has been modified' % name)

def show():
    global root
    if root == None:
        print('No student record!')
        return
    print('\n=====SHOW DATA=====')
    inorder(root)

def access(name, score):
    global root
    node = None
    prev = None
    
    if search(name) != None:
        print('Student %s has existed!' % name)
        return

    ptr = Student()
    ptr.name = name
    ptr.score = score
    ptr.llink = None
    ptr.rlink = None  

    if root == None:
        root = ptr
    else:
        node = root
        while node != None:
            prev = node
            if ptr.name < node.name:
                node = node.llink
            else:
                node = node.rlink
        
        if ptr.name < prev.name:
            prev.llink = ptr
        else:
            prev.rlink = ptr

def remove(name):
    global root
    del_node = search(name)

    if del_node == None:
        print('Student %s not found!' % name)
        return
    # 節點不為樹葉節點的狀況
    if del_node.llink != None or del_node.rlink != None:
        del_node == replace(del_node)
    else:
        if del_node == root:
            root = None
        else:
            connect(del_node, 'n')

    del_node = None # 釋放記憶體
    print('Student %s has been deleted!' % name)

# 搜尋一般節點
def search(target):
    global root
    node = root
    while node != None:
        if target == node.name:
            return node
        elif target < node.name:    # target小於目前節點，往左搜尋
            node = node.llink
        else:                       # target大於目前節點，往右搜尋
            node = node.rlink
    return node

# 尋找刪除非樹葉節點的替代節點
def replace(node):
    re_node = None
    re_node = search_re_r(node.rlink)
    if re_node == None:
        re_node = search_re_l(node.llink)
    if re_node.rlink != None:   # 當替代節點有右子樹存在的狀況
        connect(re_node, 'r')
    elif re_node.llink != None: # 當替代節點有左子樹存在的狀況
        connect(re_node, 'l')
    else: # 當替代節點為樹葉節點的狀況
        connect(re_node, 'n')

    node.name = re_node.name
    node.score = re_node.score
    return re_node

# 調整二元搜尋樹的鏈結，
# r 表示處理右鏈結、l 表示處理左鏈結、n 則將鏈結指向None
def connect(node, link):
    parent = search_p(node)        # 搜尋父節點
    if node.name < parent.name:    # 節點為父節點左子樹的狀況
        if link == 'r':
            parent.llink = node.rlink
        elif link == 'l':
            parent.llink = node.llink
        else:
            parent.llink = None
    
    elif link == 'r': # 節點為父節點右子樹的狀況
        parent.rlink = node.rlink
    elif link == 'l': # link 為 l
        parent.rlink = node.llink
    else:
        parent.rlink = None

# 搜尋右子樹替代節點
def search_re_r(node):
    re_node = node
    while re_node != None and re_node.llink != None: # 找右子樹最小值
        re_node = re_node.llink
    return re_node

# 搜尋左子樹替代節點
def search_re_l(node):
    re_node = node
    while re_node != None and re_node.rlink != None: # 找左子樹最大值
        re_node = re_node.rlink
    return re_node

# # 搜尋替代節點的父節點
def search_p(node):
    global root
    parent = root

    while parent != None:
        if node.name < parent.name:
            if node.name == parent.llink.name:
                return parent
            else:
                parent = parent.llink
        elif node.name == parent.rlink.name:
            return parent
        else:
            parent = parent.rlink
    return None

# 以中序法輸出資料，採遞迴方式
def inorder(node):
    if node != None:
        inorder(node.llink)
        print('%-15s %-3d' % (node.name, node.score))
        inorder(node.rlink)

def main():
    option = ''
    while True:
        print()
        print('**************************')
        print('       <1> insert         ')
        print('       <2> delete         ')
        print('       <3> modify         ')
        print('       <4> show           ')
        print('       <5> quit           ')
        print('**************************')

        try:
            option = input('Enter your choice: ')
        except ValueError:
            print('Not a correct number.')
            print('Try again\n')

        if option == '1':
            insert()
        elif option == '2':
            delete()
        elif option == '3':
            modify()
        elif option == '4':
            show()
        elif option == '5':
            sys.exit(0)
        else:
            print('Wrong option!')

main()
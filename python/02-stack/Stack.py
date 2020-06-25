# push, pop(delete from top), list

import sys

MAX = 10
# create list with 10 empty field 
stack = [''] * MAX
top = -1

def push():
    global MAX
    global stack
    global top

    if top >= MAX - 1:
        print("\n Stack is full")
    
    else :
        top += 1
        stack[top] = input("\n Enter a number :")
        print("stack =", stack)
    print()

def pop():
    global stack
    global top

    if top < 0:
        print("\n Stack is empty")

    else :
        print("\n %s hava been deleted " % stack[top])
        top -= 1
    print()

def list_stack():
    global stack
    global top

    count = 0

    if top < 0:
        print("\n Stack is empty")

    else:
        print("\n Data in the Stack")
        print("-----------------")
        i = top
        while i >= 0:
            print(stack[i])
            count += 1
            i -= 1
        print("-----------------")
        print("%d data in Stack" % count)
    print()

def main():
    option = 0 

    while True:
        print('***** Option *****')
        print('      1. Insert      ')
        print('      2. Delete      ')
        print('      3. List        ')
        print('      4. Exit        ')
        print('*********************')

        try:
            option = eval(input('   請選擇您要執行的項目：'))
        except ValueError:
            print('Not a correct number.')
            print('Try again\n')

        if option == 1:
            push() # 新增函數
        elif option == 2:
            pop() # 刪除函數
        elif option == 3:
            list_stack() # 輸出函數
        else:
            sys.exit(0)

main()
// use array to 
class Stack {
    constructor(){
        this.list = []
    }

    push(item){
        this.list.push(item)
    }
    pop(){
        return this.list.pop()
    }
    top(){
        return this.list[this.list.length - 1]
    }
    size(){
        return this.list.length
    }
    clear(){
        this.list = []
    }
    show(){
        return this.list
    }
}

let stack = new Stack()
stack.push('01')
stack.push('02')
console.log(stack.show())

stack.pop()
console.log(stack.show())

console.log(stack.top())
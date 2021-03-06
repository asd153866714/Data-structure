class Queue{
    constructor(){
        this.list = []
    }
    enqueue(element, priority){
        if (priority){
            this.list.splice(priority-1, 0, element)
        } else {
            this.list.push(element)
        }
    }
    dequeue(){
        this.list.shift()
    }
    size(){
        return this.list.length
    }
    front(){
        return this.list[0]
    }
    rear(){
        return this.list[this.list.length - 1]
    }
    clear(){
        this.list = []
    }
    show(){
        return this.list
    }
}

let myQueue = new Queue()

myQueue.enqueue('01')
myQueue.enqueue('02')
myQueue.enqueue('03')
myQueue.enqueue('p1', 3)
myQueue.enqueue('p0', 1)
console.log(myQueue.show())

myQueue.dequeue()
console.log(myQueue.show())

console.log(myQueue.front())
console.log(myQueue.rear())
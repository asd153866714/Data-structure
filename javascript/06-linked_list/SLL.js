// Single Linked List 
class Node{
    constructor(value){
        this.value = value
        this.next = null
    }
}
class SingleLinkedList{
    constructor(){
        this.head = null
        this.tail = null
        this.length = 0
    }

    append(value){
        let newNode = new Node(value)

        if (this.head == null){
            this.head = newNode
            // this.tail = newNode
        } else {
            let current = this.head
            while (current.next != null){
                current = current.next
            }
            current.next = newNode
        }
        this.length++
    }

    insert(position, value){
        if (position >= 0 && position < this.length){
            let newNode = new Node(value)
            let current = this.head

            if (position == 0){
                newNode.next = current
                this.head = newNode
            } else {
                let prev
                let index = 0
                while (index != position) {
                    index ++
                    prev = current
                    current = current.next
                }
                newNode.next = current
                prev.next = newNode
            }
            this.length ++
            return true
        } else {
            return false
        }

    }

    removeAt(position){
        if (position >= 0 && position < this.length){
            let current = this.head
            if (position == 0){
                this.head = head.next
            } else {
                let index = 0
                let prev
                while (position != index){
                    index ++
                    prev = current
                    current = current.next
                }
                prev.next = current.next
            }
            this.length --
            return current.value
        } else {
            return false
        }
    }

    remove(value){
        let index = this.indexOf(value)
        return this.removeAt(index)
    }

    modify(value){
        let foundNode = this.indexOf(value)

        if (foundNode){
            foundNode.value = value
        } else {
            return false
        }
    }

    indexOf(value){
        let index = 0
        let current = this.head
        while (current) {
            if (current.value == value){
                return index
            }
            current = current.next
            index ++
        }
        return false
    }

    show(){
        let count = 0
        if (this.length == 0){
            console.log('no record')
            return false
        } else {
            let current = this.head
            while (current != null) {
                console.log(current)
                current = current.next
                count ++
            }
        }
    }

    size(){
        return this.length
    }
}

let newList = new SingleLinkedList()
newList.append(01)
newList.append(02)
newList.append(03)
newList.append(04)

newList.show()
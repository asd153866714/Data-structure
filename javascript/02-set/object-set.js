class MySet {
    constructor(){
        this.items = {}
    }
    // 新增
    add(value){
        if(!this.has(value)){
            this.items[value] = value
        }
    }
    // 修改
    modify(oldValue, newValue){
        if(this.has(oldValue)){
            delete this.items[oldValue]
            this.items[newValue] = newValue
            return true
        } else {
            return false
        }
    }
    // 刪除
    delete(value){
        if(this.has(value)){
            delete this.items[value]
            return true
        }
        return false
    }
    // 判斷集合是否元素
    has(value){
        return this.items.hasOwnProperty(value)
    }
    // 清空集合
    clear(){
        this.items = {}
    }
    // 集合元素數量
    size(){
        return Object.keys(this.items).length
    }
    // 印出集合所有的元素
    list(){
        return Object.keys(this.items)
    }
}

let set = new MySet()

set.add('01')
set.add('01')
set.add('02')
set.add('03')
console.log('after add:', set.list())

set.modify('01', '10')
console.log('after modify:', set.list())

set.delete('10')
console.log('after delete:', set.list())

set.clear()
console.log('after clear:', set.list(),'\nsize:', set.size())
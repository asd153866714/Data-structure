// Simple Tree
class TreeNode {
    constructor(value) {
        this.valiue = value
        this.descendents = []
    }
}

const myTree = new TreeNode('A')
const b = new TreeNode('B')
const c = new TreeNode('C')
const d = new TreeNode('D')
const e = new TreeNode('D')

myTree.descendents.push(b)

b.descendents.push(c, d, e)

console.log(myTree)

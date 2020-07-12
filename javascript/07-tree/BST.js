// Binary Search Tree
class TreeNode {
    constructor(value) {
        this.value = value
        this.left = null
        this.right = null
    }
}

class BinarySearchTree {
    constructor() {
        this.root = null
        this.size = 0
    }

    insert(value){
        let newNode = new TreeNode(value)
        let prev = null
        if (this.search(value)) {
            console.log(`same valueL: ${value} has existed`)
            return false
        }

        if (this.root == null) {
            this.root = newNode
        } else {
            let node = this.root
            while (node != null ) {
                prev = node
                if (newNode.value < node.value) {
                    node = node.left
                } else {
                    node = node.right
                }
            }
            if (newNode.value < prev.value) {
                prev.left = newNode
            } else {
                prev.right = newNode
            }
        }
    }

    remove(value){
        if (this.root == null) {
            console.log('no record')
            return false
        }
        // search del_node
        let del_node = this.search(value)
        if (del_node == null) {
            console.log(`value: ${value} not found`)
            return false
        }
        // del_node is not leaf
        if (del_node.left != null || del_node.right != null) {
            del_node = this.replace(del_node)
        } else {
            if (del_node == this.root) {
                this.root = null
            } else {
                this.connect(del_node, 'n')
            }
        }
        console.log(`value: ${value} has been deleted`)
    }

    modify(oldValue, newValue){
        if (this.root == null) {
            console.log('no record')
            return false
        } else {
            let node = this.search(oldValue)
            if (!node) {
                console.log(`oldValue: ${oldValue} not found`)
            } else {
                console.log(`original oldValue: ${oldValue}`)
                node.value = newValue
                console.log(`newValue: ${node.value}`)
            }
        }
    }
    
    show() {
        let node = this.root
        if (node == null) {
            console.log('no record')
            return
        } 
        this.inorder(node)
    }

    inorder(node) {
        if (node != null) {
            this.inorder(node.left)
            console.log(`${node.value}`)
            this.inorder(node.right)
        }
    }

    search(target){
        let node = this.root
        while (node != null) {
            if (target == node.value){
                return node
            }
            else if (target < node.value){
                node = node.left
            }
            else {
                node = node.right
            }
        }
        return node
    }

    replace(node) {
        let replace_node = null
        if (this.search_replace_right(node.right) != null) {
            replace_node = this.search_replace_right(node.right)
        } else {
            replace_node = this.search_replace_left(node.left)
        }
        
        if (replace_node.right != null) {
            this.connect(replace_node, 'r')
        } else if (replace_node.left != null) {
            this.connect(replace_node, 'l')
        } else {
            this.connect(replace_node, 'n')
        }
        
        node.value = replace_node.value
        return node
    }

    search_replace_right(node) {
        let replace_node = node
        while (replace_node != null && replace_node.left != null) {
            replace_node = replace_node.left
        }
        return replace_node
    }

    search_replace_left(node) {
        let replace_node = node
        while (replace_node != null && replace_node.right != null) {
            replace_node = replace_node.right
        }
        return replace_node
    }

    search_parent(node) {
        let parent = this.root

        while (parent != null) {
            if (node.value < parent.value) {
                if (node.value == parent.left.value) {
                    return parent
                } else {
                    parent = parent.left
                }
            }
            else if (node.value == parent.value) {
                return parent
            }
            else {
                parent = parent.right
            }
        }
        return null
    }

    connect(node, link) {
        let parent = this.search_parent(node)
        if (node.value < parent.value) {
            if (link == 'r') {
                parent.left = node.right
            }
            else if (link == 'l') {
                parent.left = node.left
            }
            else {
                parent.left = null
            }
        }
        else if (node.value < parent.value){
            if (link == 'r') {
                parent.right = node.right
            }
            if (link == 'l') {
                parent.right = node.left
            }
            else {
                parent.right = null
            }
        }
    }
}

var myTree = new BinarySearchTree()
myTree.insert(5)
myTree.insert(9)
myTree.insert(2)
myTree.insert(3)
myTree.insert(10)
myTree.insert(1)
myTree.remove(1)
myTree.show()
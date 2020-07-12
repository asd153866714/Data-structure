var relativeSortArray = function(arr1, arr2) {
    let map1 = new Map()
    let result = []
    
    arr1.sort((a, b) => a-b)
    
    arr2.forEach(item => {
        map1.set(item, 0)
    })

    arr1.forEach(item => {
        if (map1.has(item)){
            map1.set(item, map1.get(item) + 1)
        } else {
            map1.set(item, 1)
        }
    })

    map1.forEach((value, key) => {
        for (let i=0; i<value; i++){
            result.push(key)
        }
    })

    return result

}

let arr1 = [2,3,1,3,2,4,6,7,9,2,19]
let arr2 = [2,1,4,3,9,6]
console.log(relativeSortArray(arr1, arr2))
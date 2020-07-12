const union = (set1, set2) => {
    return new Set([...set1, ...set2])
}

const intersection = (set1, set2) => {
    let interSet = new Set()
    set1.forEach(i => {
        if (set2.has(i)){
            interSet.add(i)
        }
    })
    return interSet
}

const subtraction = (set1, set2) => {
    let subSet = new Set(set1)
    set2.forEach(i => {
        if (subSet.has(i)){
            subSet.delete(i)
        }
    })
    return subSet
}

const difference = (set1, set2) => {
    let difSet = union(set1, set2)
    let interSet = intersection(set1, set2)

    difSet.forEach((i) => {
        if(interSet.has(i)){
            difSet.delete(i)
        }
    })
    return difSet

}

let a = new Set([1, 2, 3])
let b = new Set([2, 3, 4, 5, 6])

console.log('a:', a, '\nb:', b)

let c = union(a, b)
console.log('\nunion:', c)

let d = intersection(a, b)
console.log('intersection:', d)

let e = subtraction(a, b)
console.log('subtraction:', e)

let f = difference(a, b)
console.log('difference:', f)
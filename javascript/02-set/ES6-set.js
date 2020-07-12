// ES6 Set

let set = new Set(['1', '2', '3'])

set.add('01')
set.add('02')
set.add('01')
set.has('03')   // false
set.delete('01')
console.log(set.size)

console.log(Array.from(set))
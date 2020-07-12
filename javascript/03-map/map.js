// ES6 Map
const myMap = new Map()

var keyString = 'I am a string',
    keyObj = {},
    keyFunc = function(){}
    keyNumber = 1

// 增加
myMap.set(keyString , 'string value');
myMap.set(keyObj, {obj: 1});
myMap.set(keyFunc , function(){console.log('I am function')});
myMap.set(keyNumber , 100);


// 取值
let a = myMap.get(keyObj); // {obj: 1}
console.log(a);

// 看是否存在
let b = myMap.has(keyString ); //  true
console.log(b);

// 刪掉
myMap.delete(keyNumber); 
console.log(myMap.size); // 3

// 有幾個
let c = myMap.size; // 4
console.log(c);

// 轉陣列
[...myMap.values()] // ["string value", {obj: 1}, ƒ]
console.log(myMap);
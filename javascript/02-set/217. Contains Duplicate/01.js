var containsDuplicate = function(nums) {
    console.log(new Set(nums))
    return new Set(nums).size < nums.length
};

let a = containsDuplicate([1,2,3,1])
console.log(a)
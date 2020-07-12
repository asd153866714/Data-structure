var arrayPairSum = function(nums) {
    const len = nums.length
    let result = 0
    nums = nums.sort((a, b) => a-b)
    for (let i=0; i < len; i+=2){
        result += Math.min(nums[i], nums[i+1])
    }
    return result
};

console.log(arrayPairSum([1,4,3,2]))
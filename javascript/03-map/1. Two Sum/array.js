var twoSum = function(nums, target){
    const len = nums.length
    for (let i=0; i<len; i++){
        let a = nums.indexOf(target -  nums[i])
        if (a >= 0 && a != i){
            return [i, a]
        }
    }
}

// Given nums = [2, 7, 11, 15], target = 9,
console.log(twoSum([2, 7, 11, 15], 9))
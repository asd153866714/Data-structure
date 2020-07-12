var twoSum = function(nums, target){
    const map = new Map()

    for(var i=0; i<nums.length; i++){
        let value = target - nums[i]
        if (map.get(nums[i]) === undefined){
            map.set(value, i)
        } else {
            return [map.get(nums[i]), i]
        }
    }
}

// Given nums = [2, 7, 11, 15], target = 9,
console.log(twoSum([2, 7, 11, 15], 9))
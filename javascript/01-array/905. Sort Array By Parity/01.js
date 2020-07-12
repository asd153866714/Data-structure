/*
Given an array A of non-negative integers, 
return an array consisting of all the even elements of A, 
followed by all the odd elements of A.

You may return any answer array that satisfies this condition.

input: 給一個沒有負數的數字陣列
output: 回傳前面是偶數後面是奇數的陣列

Example 1:

Input: [3,1,2,4]
Output: [2,4,3,1]
The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

Note:

1 <= A.length <= 5000
0 <= A[i] <= 5000
*/

/**
 * @param {number[]} A
 * @return {number[]}
 */
var sortArrayByParity = function(A) {
    if (A.length < 2) {
        return A
    }
    let B = []
    
    A.forEach(a => {
        if (a % 2 == 0){
            B.unshift(a)
        } else {
            B.push(a)
        }
    })
    return(B)
};

sortArrayByParity([1,2,3,4])
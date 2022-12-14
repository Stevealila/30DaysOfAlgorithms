/*
Question: Leetcode 268
Link: https://leetcode.com/problems/missing-number/
*/

const missingNumber = arr => {
    let output = arr.length
    for(let i in arr) output += (i - arr[i])
    return output
}

let nums = [3, 0, 1]
console.log(missingNumber(nums)) // 2
nums = [0, 1]
console.log(missingNumber(nums)) // 2
nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
console.log(missingNumber(nums)) // 8
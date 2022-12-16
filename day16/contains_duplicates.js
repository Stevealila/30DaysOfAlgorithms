/*
Question: Leetcode 217
Link: https://leetcode.com/problems/contains-duplicate/

This implimentation applies an hash map, also known as object in JavaScript.
Loop through the array,
Checking if the current element exists in the hash map before adding it to the hash map. 
If the element already exists in the hash map, return true. 

*/
const containsDuplicates  = arr => {

    hm = {}
    
    for (let n of arr) {
        if (n in hm) return true
        hm[n] = n 
    }
    
    return false
}



let nums = [1,2,3,1]
console.log(containsDuplicates(nums)) //true

nums = [1,2,3,4]
console.log(containsDuplicates(nums)) //false
nums = [1,1,1,3,3,4,3,2,4,2]

console.log(containsDuplicates(nums))//true
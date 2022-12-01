/*
Move sequentially from left to right UNTIL you find the target. 
The target does not exist if you visit all elements without finding it.

Runs in 0(n)
*/

const linearSearch = (arr, target) => {
    for (let n of arr) if (n === target) return true
    return null
}

const arr = [23, 19, 29, 31, 47, 37]

const target = 19
const target2 = 39

console.log(linearSearch(arr, target)) // true
console.log(linearSearch(arr, target2)) // null
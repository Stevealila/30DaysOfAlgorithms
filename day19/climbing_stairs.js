/*
    Question: Leetcode 70
    Link: https://leetcode.com/problems/climbing-stairs/

    This implementation relies on the Bottom-up Dynamic Programming technique.
*/

const climbingStairs = n => {
    let one = 1, two = 1

    for (let i = 0; i < n - 1; i++) {
        tempOne = one 
        one += two
        two = tempOne
    }

    return one
}

let n = 2
console.log(climbingStairs(n)) //2
n = 3
console.log(climbingStairs(n)) //3
n = 7
console.log(climbingStairs(n)) //21

/*
    Question: Leetcode 374
    Link: https://leetcode.com/problems/guess-number-higher-or-lower/

    This implementation applies binary search.
    (https://github.com/Stevealila/30DaysOfAlgorithms/blob/main/day3/iterativeBinary.py)
*/


const guessNumber = (upperBound, target) => {
    let left = 1, right = upperBound

    while (left <= right) {
        mid = Math.floor((left + right) / 2)

        if (mid === target) return mid 
        if (mid < target) left = mid + 1
        else right = mid - 1
    }
}


let n = 10, pick = 6
console.log(guessNumber(n, pick)) //6

n = 1, pick = 1
console.log(guessNumber(n, pick)) //1

n = 2, pick = 1
console.log(guessNumber(n, pick)) //1
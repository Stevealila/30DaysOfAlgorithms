/*
Keep slicing the sorted data structure into two portions, 
while searching in the portion that is likely to contain the target.

Return true if the target is found. Otherwise, return null.

Runs in 0(log n).
*/

const binarySearch = (array, target) => {

    if (array.length === 0) return null 

    let midpoint = Math.floor( (array.length - 1)/2 )

    let leftArray = array.slice(0, midpoint),
        rightArray = array.slice(midpoint + 1)
                
    if (array[midpoint] === target) 
        return true
    else if (array[midpoint] > target) 
        return binarySearch(leftArray, target)
    else 
        return binarySearch(rightArray, target)
        
}


const array = [19, 23, 29, 31, 37, 41, 47]

console.log(binarySearch(array, 29)) //true
console.log(binarySearch(array, 9)) //null
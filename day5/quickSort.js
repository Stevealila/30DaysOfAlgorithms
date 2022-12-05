/*
Relies on the Divide and Conquer.

Divide: Locate the pivot element (can be any element. I have picked the first one). 
        Create an empty left array and an empty right array.
        Politely ask any element less than the pivot to take a seat in the left room. 
        Likewise, elements greater than the pivot to move to the right array.
        Repeat the process until you cannot subdivide a subarray.
Conquer: Congratulations! You successfully sorted the elements while splitting them. 
         Now merge the sorted elements into the previous subarrays.
         Repeat the process until the original array is filled with sorted elements.

*/

const quickSort = arr => {
    
    if (arr.length <= 1) return arr 
    
    let pivot = arr[0],
        leftArray = [],
        rightArray = []

    // split the array
    for (let i = 1; i < arr.length; i++) {
        if (arr[i] <= pivot) 
            leftArray.push(arr[i])
        else 
            rightArray.push(arr[i])
    }
    
    // merge the sorted subarrays
    return [...quickSort(leftArray), pivot, ...quickSort(rightArray)]
}



const arr = [24, 15, 58, 55, 43, 19]
console.log(quickSort(arr)) // [15, 19, 24, 43, 55, 58]
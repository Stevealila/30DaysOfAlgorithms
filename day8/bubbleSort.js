/*
swap elements till the entire array is sorted. 
Minimize the sort space for subsequent iterations 
since we don't revisit the sorted (last) element.

Runs in 0(n^2)
*/

const bubbleSort = arr => {
    for (let i = 0; i < arr.length; i++) {
        for (let j = 0; j < arr.length - 1; j++) {
            // swap the elements
            if (arr[j] > arr[j+1]) {
                let tmp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = tmp
            }
        }   
    }

    return arr
}


const arr = [13, 19, 17, 23, 11] 
console.log(bubbleSort(arr)) //[ 11, 13, 17, 19, 23 ]




/*
Relies on the Divide and Conquer Technique.

Divide: Recursively split the array into left and right subarrays
Conquer: merge back the subarrays starting with the smallest portion

Runs in 0(n log n)
*/


const mergeSort = (arr) => {
    // We have no work to do since an empty or a single-element array is naively sorted.
    if (arr.length <= 1) return arr

    // split the array
    let unsortedLeft = arr.slice(0, Math.floor(arr.length / 2)),
        unsortedRight = arr.slice(Math.floor(arr.length / 2), arr.length)

    // merge-sort the left and right subarrays
    let leftArray = mergeSort(unsortedLeft),
        rightArray = mergeSort(unsortedRight)
    return merge(leftArray, rightArray)
}

const merge = (leftArray, rightArray) => {
    const sortedArray = []

    let l = 0, r = 0

    // let's decide who takes the first seat in the new sorted array
    while (l < leftArray.length && r < rightArray.length){

        /*
        Is the left subarray's first element larger than the right's? 
        If yes, it goes first. And replace the empty space with the next left element. 
        Otherwise, the right subarray's element goes first. And replace the empty space with the next right element.
        */
        if (leftArray[l] < rightArray[r]){
            sortedArray.push(leftArray[l])
            l++
            // 
        } else {
            sortedArray.push(rightArray[r])
            r++
        }
    }

    /*
    What if element(s) still remain in either subarray, while the other subarray's elements have all joined the sorted array?
    We have no other option, but to append the pending subbarry's elements into the sorted array.
    */
    while (l < leftArray.length){
        sortedArray.push(leftArray[l])
        l++

    }

    while (r < rightArray.length){
        sortedArray.push(rightArray[r])
        r++
    }


    return sortedArray
}




const arr = [24, 15, 58, 55, 43, 19]
console.log(mergeSort(arr)) // [ 15, 19, 24, 43, 55, 58 ]

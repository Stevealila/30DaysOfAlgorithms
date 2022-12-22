/*
    Store the current element in a temporary container.
    Sort the left portion of the current element until all element are in place.

    Runs in 0(n^2)
*/

const insertionSort = arr => {
    for (let i = 1; i < arr.length; i++) {
        tmp = arr[i]
        j = i - 1
        // sort the left portion
        while (j >= 0 && arr[j] > tmp) {
            arr[j + 1] = arr[j]
            j--;
        }
        // update the temporary container
        arr[j + 1] = tmp
    }

    return arr
}



let arr = [7, 4, 6, 5, 9]
console.log(insertionSort(arr)) // [ 4, 5, 6, 7, 9 ]

arr = ['Mario', 'Smith', 'Abdi', 'Mariam', 'Chan']
console.log(insertionSort(arr)) // [ 'Abdi', 'Chan', 'Mariam', 'Mario', 'Smith' ]


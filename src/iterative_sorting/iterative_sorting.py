# # TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index

        for j in range(cur_index, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        
        temp = arr[smallest_index]
        arr[smallest_index] = arr[cur_index]
        arr[cur_index] = temp
    return arr

# # TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    # Loop through your array
    # Compare each element to its neighbor
    # If elements in wrong position (relative to each other, swap them)
    # If no swaps performed, stop. Else, go back to the element at index 0 and repeat step 1.
    for i in range(len(arr)):
       for j in range(len(arr) - i - 1):
           if arr[j + 1] < arr[j]:
               arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

print(bubble_sort([6,3,8,2,1,9]))

# # STRETCH: implement the Count Sort function below
# def count_sort( arr, maximum=-1 ):

#     return arr
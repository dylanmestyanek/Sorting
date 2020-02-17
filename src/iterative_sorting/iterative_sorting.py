# # TO-DO: Complete the selection_sort() function below 
# def selection_sort( arr ):
#     for i in range(0, len(arr) - 1):
#         cur_index = i
#         smallest_index = cur_index

#         for j in range(cur_index, len(arr)):
#             if arr[j] < arr[smallest_index]:
#                 smallest_index = j
        
#         temp = arr[smallest_index]
#         arr[smallest_index] = arr[cur_index]
#         arr[cur_index] = temp
#     return arr

# print(selection_sort([0, 1, 2, 3, 4, 5, 6, 8, 9, 7]))

# # TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    # Loop through your array
    # Compare each element to its neighbor
    # If elements in wrong position (relative to each other, swap them)
    # If no swaps performed, stop. Else, go back to the element at index 0 and repeat step 1.
    swapped = True

    while swapped != False:
        swapped = True
        for i in range(0, len(arr) ):
            if arr[i + 1] < arr[i]:
                switch1 = arr[i + 1]
                switch2 = arr[i]
                arr[i] = switch1
                arr[i + 1] = switch2
                print("INDEX", i, "ARR", arr)

         


    return arr

print(bubble_sort([6,3,8,2,1,9]))

4,3,2,1
3,4,2,1,
3,2,4,1
3,2,1,4

2,3,1,4
2,1,3,4

# # STRETCH: implement the Count Sort function below
# def count_sort( arr, maximum=-1 ):

#     return arr
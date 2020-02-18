def bubblesort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

# print(bubblesort([1,3,2,7,9]))

def selection_sort(arr):
    for i in range(len(arr)):
        smallest = i

        for j in range(i, len(arr)):
            if arr[j] < arr[i]:
                smallest = j
        
        arr[smallest], arr[i] = arr[i], arr[smallest]

    return arr


print(selection_sort([1,3,2,8,7,9, 11, 10, 8231, 394, 4]))
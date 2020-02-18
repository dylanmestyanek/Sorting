# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements

    a = b = r = 0
    while a < len(arrA) and b < len(arrB):
    
        if (arrA[a] < arrB[b]):
            merged_arr[r] = arrA[a]
            a += 1
            r += 1
        else:
            merged_arr[r] = arrB[b]
            b += 1
            r += 1

    while a < len(arrA):
        merged_arr[r] = arrA[a]
        a += 1
        r += 1

    while b < len(arrB):
        merged_arr[r] = arrB[b]
        b += 1
        r += 1

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    if len(arr) > 1:
        left = merge_sort(arr[0 : len(arr) // 2])
        right = merge_sort(arr[len(arr) // 2 :])
        arr = merge(left, right)
    return arr

print(merge_sort([4,3,2,1,8,1,3,10, 11]))


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr

# STRETCH: implement Linear Search				
def linear_search(arr, target):
  
  # TO-DO: add missing code
    for i in range(len(arr)):
          if arr[i] == target:
                return arr.index(target)
    return -1 

# STRETCH: write an iterative implementation of Binary Search 
def binary_search(arr, target):

    if len(arr) == 0:
      return -1 # array empty
      
    low = 0
    high = len(arr)-1
    found = False

    while low <= high and not found:
        middle = (high + low) // 2
          
        if arr[middle] == target:
              found = True
              return arr.index(target)
        else:
            if arr[middle] > target:
                  high = middle - 1
            else:
                  low = middle + 1

    return -1 # not found

# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low, high):
  
  middle = (low+high)//2

  if len(arr) == 0:
    return -1 # array empty
  # TO-DO: add missing if/else statements, recursive calls

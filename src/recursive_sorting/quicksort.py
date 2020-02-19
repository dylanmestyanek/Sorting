# Quicksort Babyyyyyyyyy

# [5, 9, 3, 7, 2, 8, 1, 6]

# Pick a pivot 
# Find values that are smaller and bigger than your pivot and put them on their own sides of the pivot
# [3, 2, 1] [5] [9, 7, 8, 6]

# Sort left by choosing a new pivot, and repeating the original steps
# [3] is new pivot on left
# [9] is new pivot on right

# [2, 1][3][NOTHING ON RIGHT OF 3][5][7,8,6][9][NOTHING ON RIGHT OF 9]
# [2,1][3][][5][7,8,6][9][]

# rinse and repeat


# 1.) Decide on a base case
    # Base case is an empty list: []

# 2.) Find the pivot point
# 3.) Separate smaller/larger values around pivot (Smaller -> left, Larger -> right)
# 4.) Rinse + Repeat

numbahsss = [5, 9, 3, 7, 2, 8, 1, 6]

def separate_values(data):
    left = []
    pivot = data[0]
    right = []

    for item in data[1:]:
        if item < pivot:
            left.append(item)
        else: # Also handles scenario where the item equals the pivot
            right.append(item)

    return left, pivot, right

def quicksort(data):
    if len(data) == 0:
        return data

    left, pivot, right = separate_values(data)

    return quicksort(left) + [pivot] + quicksort(right)

print(quicksort([2,4,1,9,5,1,1,53]))
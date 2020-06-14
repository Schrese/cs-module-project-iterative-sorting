def linear_search(arr, target):
    # Your code here
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    # store high
    high = len(arr) -1
    # store low
    low = 0

    # as long as high and low values aren't the same, keep going
    # while low != high: # This doesn't work, i forgot about negative numbers, luckily tests gave me that hint
    while low <= high:
        # mid is always going to be equal to high+low/2
        mid = (low + high) // 2
        # guess will always be index mid
        guess = arr[mid]
        # if guess is correct, return the index
        if guess == target:
            return mid
        # if guess is too high
        if guess > target:
            # set high to mid - 1 (the '-1' takes the mid into account) 
            high = mid - 1
        # if guess is too low
        if guess < target:
            # set low to mid + 1 (the '+1' takes the mid into account)
            low = mid + 1

    return -1  # not found

#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)0(n)
changes according to input size

b)0(2^n)
because of nested loops

c)0(n)
even though it is using recursion it is only
decrementing by 1, so it is acting as a loop and 
that is 0(n)


## Exercise II
Binary Search is the best method for broken eggs!
It is O(log n) because the input size is decreased at each step.
def binarySearch(input, high = None, low = None):
    low = 0
    high = len(input) -1 
    mid = (low + high)//2
    if input[mid] == input[high] or input[mid] == input[low]: 
        print('eggs not broken on this floor')
        return input[mid]
    if input[mid] < input[high]:
        print('eggs broken') 
        high - 1
    else: 
        print('eggs broken')
        low + 1
    return binarySearch(input[mid], high, low)
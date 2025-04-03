## Linear Search:
# Best Case:  O(n) => O(1)
# Worst Case: O(n) => O(7)
#############################
## Binary Search:
# O(log n)

def binarySearch(array,query ,lowIndex , highIndex):
    while lowIndex <= highIndex:
        mid = lowIndex + (highIndex - lowIndex) // 2 
        if array[mid] == query:
            return mid
        elif array[mid] < query:
            lowIndex = mid + 1
        else: 
            highIndex = mid - 1
    return -1

grades = [10 , 11 , 14 , 15 , 16 , 17 , 20] # Length : 7
search = 20
result = binarySearch(grades , search , 0 , len(grades)- 1)

if result == -1 :
    print("Not Found")
else:
    print("Found")
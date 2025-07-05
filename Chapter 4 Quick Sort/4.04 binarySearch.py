# my implementation of binary search using recursion

sortedList = [1,2,3,4,5]

def binarySearch(myList, num):
    start = 0
    end = len(myList) - 1
    midValue = myList[(start + end) // 2]
    print(midValue)
    if midValue == num:
        return midValue
    
    elif midValue < num:
        return binarySearch(myList[midValue:], num)
    
    else:
        return binarySearch(myList[:midValue,num])
    

binarySearch(sortedList, 5)
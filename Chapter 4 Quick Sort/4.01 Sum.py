# this function adds numbers in a list using recursion

someList = [1,2,3,4,5,6,7,8,9]

def sum(myList):
    if len(myList) == 1:
        return myList[0]
    else:
        return myList.pop() + sum(myList)

print(sum(someList))
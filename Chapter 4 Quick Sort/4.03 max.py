# this function uses a recursion to find the maximum number in a list

someList = [10,2,3,2,5]

def max(myList):
    try:
        mynum = myList.pop()
        nextNum = max(myList)
        if mynum >= nextNum:
            return mynum
        else:
            return nextNum
    except:
        return 0
    

print(max(someList))
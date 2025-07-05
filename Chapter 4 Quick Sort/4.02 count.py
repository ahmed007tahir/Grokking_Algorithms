# this function counts the number of items in a list using recurssion

someList = [1,2,3,"a"]
def count(myList):
    counter = 0
    try:
        myList.pop()
        counter =+ 1
        return counter + count(myList)
    except:
        return 0

        

print(count(someList))
# Binary Search is the first algorithm introduced in the book. So far I have read the theory and this is my attempt at writing my own binary search algorithm

sorted_numbers = [-1,0,3,5,9,12]

# this function takes in a number as in input and returns the index of the number in list of sorted_numbers.
def binary_search(list, number):
    start = 0
    end = len(list) - 1
    midpoint = (start + end) // 2

    while start != midpoint and end != midpoint:
        if number == list[midpoint]:
            return midpoint
        elif number < list[midpoint]:
            end = midpoint
            midpoint = (start + end) // 2
        else:
            start = midpoint
            midpoint = (start + end) // 2
print(binary_search(sorted_numbers, 9))

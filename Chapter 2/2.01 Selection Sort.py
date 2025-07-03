my_list = [54,243,54,73,14,54,76,7,34,12,16,32,64,89,6321,4856,198,561,984]

def selection_sort(unsorted_list):
    sorted_list = [] # this variable will be populated with my sorted list

    while len(unsorted_list) > 0:
        index_largest_number = 0
        for i in range(len(unsorted_list)):
            if unsorted_list[index_largest_number] > unsorted_list[i]:
                index_largest_number = i
        sorted_list.append(unsorted_list[index_largest_number])
        unsorted_list.pop(index_largest_number)

    return sorted_list

print(selection_sort(my_list))
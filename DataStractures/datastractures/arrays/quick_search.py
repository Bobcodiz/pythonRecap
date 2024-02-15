# global variable
position = []


def finder(numbers, number_to_search, start_index, end_index):
    mid = (start_index + end_index) // 2
    if start_index <= end_index:
        if numbers[mid] == number_to_search:
            position.append(mid)
        finder(numbers, number_to_search, mid + 1, end_index)
        finder(numbers, number_to_search, start_index, mid - 1)
    else:
        return


numbers = [1, 4, 6, 7, 8, 9, 11, 15, 15, 15, 17, 21, 34, 34, 56]
number_to_find = 15
finder(numbers, number_to_find, 0, len(numbers)-1)

print(position)

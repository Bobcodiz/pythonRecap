from util import timeit


def binary_search(number_to_find, numbers):
    left_index = 0
    right_index = len(numbers) - 1
    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        if numbers[mid_index] == number_to_find:
            # positions.append(mid_index)
            return mid_index
        if numbers[mid_index] < number_to_find:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1
    return None









if __name__ == '__main__':

    positions = []

    for i in numbers:
        index = binary_search(number_to_find, numbers)
        if index is None:
            break
        else:
            positions.append(index)

    print(f"Number {number_to_find} is found at index {positions}")

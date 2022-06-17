def sort_array(source_array):
    indexes = []
    odd_numbers = []
    for index, number in enumerate(source_array):
        if number % 2:
            indexes.append(index)
            odd_numbers.append(number)
    odd_numbers.sort()
    odd = 0
    for index in indexes:
        source_array[index] = odd_numbers[odd]
        odd += 1
    return source_array


if __name__ == '__main__':
    print(sort_array([5, 3, 2, 8, 1, 4]))

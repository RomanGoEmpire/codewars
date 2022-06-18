def tip1():
    data = [1, 2, -4, -3]
    for i in range(len(data)):
        if data[i] < 0:
            data[i] = 0
    print(data)

    data = [1, 2, -4, -3]
    for idx, num in enumerate(data):
        if num < 0:
            data[idx] = 0
    print(data)


def tip2():
    squares = []
    for i in range(10):
        squares.append(i * i)
    print(squares)

    squares = [i * i for i in range(10)]
    print(squares)


def tip3():
    data = [1, 6, 2, 7]
    sorted_data = sorted(data, reverse=True)
    print(sorted_data)

    data = [{"name": "Max", "age": 6},
            {"name": "Lisa", "age": 20},
            {"name": "Ben", "age": 9}]
    sorted_data = sorted(data, key=lambda x: x["age"])
    print(sorted_data)


def tip4():
    my_list = [1, 2, 3, 4, 5, 6, 7, 7, 7]
    my_set = set(my_list)
    print(my_set)

    primes = {2, 3, 5, 7, 11, 13}
    print(primes)


def tip5():
    import sys
    my_list = [i for i in range(10000)]
    print(sum(my_list))
    print(sys.getsizeof(my_list), "bytes")

    my_gen = (i for i in range(10000))
    print(sum(my_gen))
    print(sys.getsizeof(my_gen), "bytes")


def tip6():
    my_dict = {"items": "football", "price": 10.00}
    count = my_dict.get("count", 0)
    print(count)

    count = my_dict.setdefault("count",0)
    print(my_dict)


def tip7():
    from collections import Counter

    my_list = [1, 1, 1, 1, 10, 10, 10, 9, 9, 9, 9, 9]
    counter = Counter(my_list)
    print(counter)


def tip8():
    name = "Alex"
    my_string = f"Hello {name}"
    print(my_string)

    i = 10
    print(f"{i} squared is {i * i}")


def tip9():
    list_of_strings = ["Hello", "my", "friend"]

    # GOOD:
    my_string = " ".join(list_of_strings)
    print(my_string)


def tip10():
    d1 = {"name": "Alex", "age": 25}
    d2 = {"name": "Alex", "city": "New York"}
    merged_dict = {**d1, **d2}
    print(merged_dict)


def tip11():
    # simplify if statement for multiple checks

    colors = ["red", "green", "blue"]

    c = "red"
    if c in colors:
        print("is main color")


if __name__ == '__main__':
    # 1) Iterate with enumerate() instead of range(len())
    # 2) Use List Comprehensions instead of raw loops
    # 3) Sort complex iterables with sorted()
    # 4) Store unique values with Sets
    # 5) Save memory with generators
    # 6) Define default values in dictionaries with .get() and .setdefault
    # 7) Count hashable objects with collections.Counter
    # 8) Format strings with f-strings
    # 9) concat string with .join()
    # 10) merge two dictionaries(3.5+)
    # 11) simplify if statement for multiple checks

    tip6()

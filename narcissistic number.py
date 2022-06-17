def narcissistic(value):
    val = value
    result = 0
    power = 1
    while value > pow(10, power):
        power += 1
    for x in range(1, power + 1):
        result += pow(int(val % pow(10, x) / pow(10, x - 1)), power)
        val -= val % pow(10, x)
    return result == value


def narcissistic_improved(value):
    power = len(str(value))
    result = 0
    for i in str(value):
        result += pow(int(i), power)
    return result == value


if __name__ == '__main__':
    for i in range(pow(10, 10)):
        if narcissistic_improved(i):
            print(i)

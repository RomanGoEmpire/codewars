def solution(n):
    if n > 3999:
        return "not possible"
    result = ""
    length = len(str(n))
    power = length - 1
    for i in str(n):
        number = (int(i) * pow(10, power))
        if power == 3:
            result += each_power(number, "M", "M", "M", 3)
        elif power == 2:
            result += each_power(number, "C", "D", "M", 2)
        elif power == 1:
            result += each_power(number, "X", "L", "C", 1)
        else:
            result += each_power(number, "I", "V", "X", 0)
        power -= 1
    return result


def each_power(number, s1, s2, s3, power):
    ten_pow = pow(10, power)
    result = ''
    if number <= 3 * ten_pow:
        for t in range(0, number, ten_pow):
            result += s1
    elif number == 4 * ten_pow:
        result += s1 + s2
    elif 5 * pow(10, power) <= number <= 8 * ten_pow:
        result += s2
        for f in range(0, number - 5 * ten_pow, ten_pow):
            result += s1
    else:
        for t in range(0, pow(10, power + 1) - number, ten_pow):
            result += s1
        result += s3
    return result


if __name__ == '__main__':
    print(solution(346))

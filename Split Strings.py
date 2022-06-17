def solution(s):
    length = int(len(s))
    result = []
    if length % 2:
        s += '_'
    for x in range(0, length, 2):
        result.append(s[x] + s[x + 1])
    return result


if __name__ == '__main__':
    print(solution("hatasetawet"))

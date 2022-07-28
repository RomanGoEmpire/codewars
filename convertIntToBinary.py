def count_bits(N):
    number_in_binary = bin(N)[2:]
    bits = 0
    for number in number_in_binary:
        if int(number) == 1:
            bits += 1
    return bits


if __name__ == '__main__':
    print(count_bits(5))

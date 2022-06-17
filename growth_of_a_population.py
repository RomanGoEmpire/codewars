def nb_year(p0, percent, aug, p):
    year_counter = 0
    p_current = p0
    while True:
        p_next = int(p_current + p_current * percent / 100 + aug)
        year_counter += 1
        if p_next >= p:
            return year_counter
        p_current = p_next


if __name__ == '__main__':
    print(nb_year(1000, 2, 50, 1200))

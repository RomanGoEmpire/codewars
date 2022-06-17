def tower_builder(n_floors):
    tower_layer = []
    for n in range(n_floors):
        tower = ' ' * (n_floors - n - 1)
        tower += '*' * (1 + 2 * n)
        tower += ' ' * (n_floors - n - 1)
        tower_layer.append(tower)
    return tower_layer


if __name__ == '__main__':
    print(tower_builder(5))

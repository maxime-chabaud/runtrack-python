def draw_triangle(height):
    if height < 1:
        return

    for i in range(height):
        if i == height - 1:
            print('-' * (2 * height - 1))
        else:
            spaces = ' ' * (height - i - 1)
            if i == 0:
                print(spaces + '^')
            else:
                print(spaces + '/' + ' ' * (2 * i - 1) + '\\')

draw_triangle(5)

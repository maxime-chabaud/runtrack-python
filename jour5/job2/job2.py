def draw_rectangle(width, height):
    if width < 2 or height < 2:
        print("La largeur et la hauteur doivent être supérieures à 1.")
        return

    for i in range(height):
        if i == 0 or i == height -1:
            print('-' * width)
        else:
            print('|' + ' ' * (width - 2) + '|')

draw_rectangle(6, 4)

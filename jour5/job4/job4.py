def draw_rectangle(w):
    h = w
    j = 0
    print("+", "-"*(w+1), "+")
    for i in range(h+1):
        print("|", "#"*(w-j), "#"*j, "|")
        j+=1
    print("+", "-"*(w+1), "+")

draw_rectangle(9)
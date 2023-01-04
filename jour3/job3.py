def a_list(i):
    for a in range(1,i+1):
        if not (a in [26,37,88]):
            print(a)
        pass
print(a_list(100))
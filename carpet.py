def draw_carpet(w, h):
    for i in range(h):
        for j in range(w):
            if 2 >= j >= 0 or w - 3 <= j <= w - 1:
                print(u'\u2591', end='')
            elif 0 < j < w - 1 and (1 >= i >= 0 or h - 2 <= i <= h - 1) or (6 > j > 2 or w - 7 < j < w - 3) \
                    and 1 < i < h - 2:
                print(u'\u2593', end='')
            else:
                print(u'\u2592', end='')
        print()


draw_carpet(50, 50)

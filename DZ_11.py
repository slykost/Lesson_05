print(' A')
h = int(input())
w = (h * 2) - 1
for i in range(h):
    for j in range(w):
        if (
            j == h - 1 - i
            or j == h - 1 + i
            or i == w // 2
        ):
            print('* ', end='')
        else:
            print('  ', end='')
    print()

print()
print(' B')
h = int(input())
w = (h * 2) - 1
for i in range(h):
    for j in range(w):
        if (
            j == h - 1 - i
            or j == h - 1 + i
            or i == w // 2
            or h - 1 - i <= j <= h - 1 + i
        ):
            print('* ', end='')
        else:
            print('  ', end='')
    print()

print()
print(' С')
h = int(input())
if h % 2 == 0:
    h = h + 1
w = h
H = h // 2
W = w // 2
for i in range(h):
    for j in range(w):
        if i <= H:
            if (
                j == H - i
                or j == H + i
                or i == w // 2
                or H - i <= j <= H + i
            ):
                print('* ', end='')
            else:
                print('  ', end='')
        else:
            if (
                j == H - h + i + 1
                or j == H + h - i - 1
            ):
                print('* ', end='')
            else:
                print('  ', end='')
    print()

print()
print(' D')
h = int(input())
if h % 2 == 0:
    h = h + 1
w = h
H = h // 2
W = w // 2
for i in range(h):
    for j in range(w):
        if i <= H:
            if (
                j == H - i
                or j == H + i
                or i == w // 2
                or H - i <= j <= H + i
            ):
                print('* ', end='')
            else:
                print('  ', end='')
        else:
            if (
                j == H - h + i + 1
                or j == H + h - i - 1
                or j == H
            ):
                    print('* ', end='')
            else:
                print('  ', end='')
    print()
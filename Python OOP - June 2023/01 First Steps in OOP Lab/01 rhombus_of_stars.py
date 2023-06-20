def draw_rhombus(n):
    for i in range(n):
        offset = (n - i - 1) * " "
        content = ("* " * (i + 1)).strip()
        print(f"{offset}{content}")

    for j in range(n - 1, 0, -1):
        offset = (n - j) * " "
        content = ("* " * j).strip()
        print(f"{offset}{content}")


draw_rhombus(int(input()))

# Variant 2 with reusing a method
#
#
# def draw_line(count, symbol, offset_count=0):
#     offset = offset_count * " "
#     content = (f"{symbol} " * count).strip()
#     print(f"{offset}{content}")
#
#
# def draw_rhombus(n):
#     for i in range(n):
#         draw_line(i + 1, "*", n - i - 1)
#
#     for j in range(n - 2, -1, -1):
#         draw_line(j + 1, "*", n - j - 1)
#
#
# draw_rhombus(int(input()))

# Variant 3
#
#
# def print_rhombus(n):
#     for i in range(n):
#         spaces_count = n - 1 - i
#         stars_count = i + 1
#         print(" " * spaces_count + stars_count * "* ")
#     for j in range(n - 2, -1, -1):
#         spaces_count = n - 1 - j
#         stars_count = j + 1
#         print(" " * spaces_count + stars_count * "* ")
#
#
# number = int(input())
# print_rhombus(number)
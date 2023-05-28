count_input_lines = int(input())

my_set = set()

for _ in range(count_input_lines):
    elements = input().split()
    for element in elements:
        my_set.add(element)

print(*my_set, sep="\n")
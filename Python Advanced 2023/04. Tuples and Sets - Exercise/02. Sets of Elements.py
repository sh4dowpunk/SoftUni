size_of_sets = [int(x) for x in input().split()]

set_one = set()
set_two = set()

for num in range(size_of_sets[0]):
    current_num = int(input())
    set_one.add(current_num)

for num in range(size_of_sets[1]):
    current_num = int(input())
    set_two.add(current_num)

print(*set_one.intersection(set_two), sep="\n")
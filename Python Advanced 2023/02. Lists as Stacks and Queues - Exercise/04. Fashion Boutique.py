from collections import deque

clothes_in_box = deque([int(x) for x in input().split()])
rack_capacity = int(input())

racks = 1
current_rack_capacity = rack_capacity

while clothes_in_box:
    clothes = clothes_in_box.pop()

    if current_rack_capacity >= clothes:
        current_rack_capacity -= clothes
    else:
        racks +=1
        current_rack_capacity = rack_capacity - clothes

print(racks)
from collections import deque

cups = deque([int(x) for x in input().split()])
bottles = [int(x) for x in input().split()]
water = 0

while cups and bottles:
    cup = cups.popleft()
    while cup > 0:
        bottle = bottles.pop()
        cup -= bottle
        if cup <= 0:
            water += abs(cup)

if cups:
    print(f"Cups: {' '.join(map(str, cups))}")
    print(f"Wasted litters of water: {water}")
else:
    print(f"Bottles: {' '.join(map(str, reversed(bottles)))}")
    print(f"Wasted litters of water: {water}")
from collections import deque

collected_honey = 0

functions = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b
}

workings_bees = deque([int(x) for x in input().split()])    # deque([20, 62, 99, 35, 0, 150])
nectar = deque([int(x) for x in input().split()])    # deque([120, 60, 10, 1, 70, 10])
waiting_bees = deque(input().split())    # deque(['+', '-', '+', '+', '/', '*', '-', '-', '/'])

while workings_bees and nectar:
    bee = workings_bees.popleft()    # 20
    current_nectar = nectar.pop()    # 10

    if current_nectar >= bee:    # It is considered collected, the bee can return to the hive
        if current_nectar != 0:    # We can not divide by zero!
            collected_honey += abs(functions[waiting_bees.popleft()](bee, current_nectar))    # We take the first symbol

    elif current_nectar < bee:
        workings_bees.appendleft(bee)

print(f"Total honey made: {collected_honey}")
if workings_bees:
    print(f"Bees left: {', '.join(str(x) for x in workings_bees)}")
if nectar:
    print(f"Nectar left: {', '.join(str(x) for x in nectar)}")
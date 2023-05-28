from collections import deque

parenthesis = deque(input())
starting_parenthesis = deque()

while parenthesis:
    curr_parenthesis = parenthesis.popleft()

    if curr_parenthesis in "([{":
        starting_parenthesis.append(curr_parenthesis)
    elif not starting_parenthesis:
        print("NO")
        break
    else:
        if f"{starting_parenthesis.pop() + curr_parenthesis}" not in "()[]{}":
            print("NO")
            break

else:
    print("YES")
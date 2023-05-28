text = list(input())
stack_line = []

while text:
    stack_line.append(text.pop())

print("".join(stack_line))
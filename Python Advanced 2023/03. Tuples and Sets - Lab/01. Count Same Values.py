numbers = [float(n) for n in input().split()]
dictionary = {}

for num in numbers:
    dictionary[num] = numbers.count(num)

for key, value in dictionary.items():
    print(f"{key:.1f} - {value} times")
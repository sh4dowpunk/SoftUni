string = input()

dictionary = {}

for letter in string:
    if letter not in dictionary.keys():
        dictionary[letter] = 0
    dictionary[letter] += 1

for key, value in sorted(dictionary.items()):
    print(f"{key}: {value} time/s")
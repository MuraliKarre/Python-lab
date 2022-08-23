numbers = [1, 2, 3, 4, 4, 3, 2, 1]
unique = []
for number in numbers:
    if number not in unique:
        unique.append(number)
print(unique)

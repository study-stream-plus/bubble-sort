numbers = [3, 2, 6, 5, 4, 7, 8, 1, 9]
length = len(numbers) - 1
sorted = False

while not sorted:
    sorted = True

    for i in range(0, length):
        if numbers[i] > numbers[i + 1]:
            sorted = False
            numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]

print(numbers)

numbers = [1, 60, 93, 14, 52, 77, 44]

swap = True
while swap:
    swap = False
    for i in range(len(numbers)-1):
        if numbers[i] > numbers[i+1]:
            holder = numbers[i+1]
            numbers[i+1] = numbers[i]
            numbers[i] = holder
            swap = True

print(numbers)



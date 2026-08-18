# ----------- 4-3 Counting to Twenty -----------

for number in range(1, 21):
    print(number)


# ----------- 4-4 One Million -----------

numbers = list(range(1, 1_000_001))

for number in numbers:
    print(number)


# ----------- 4-5 Summing a Million -----------

numbers = list(range(1, 1_000_001))

print(min(numbers))
print(max(numbers))
print(sum(numbers))


# ----------- 4-6 Odd Numbers -----------

odd_numbers = list(range(1, 21, 2))

for number in odd_numbers:
    print(number)


# ----------- 4-7 Threes -----------

multiples_of_three = list(range(3, 31, 3))

for number in multiples_of_three:
    print(number)


# ----------- 4-8 Cubes -----------

cubes = []

for number in range(1, 11):
    cube = number ** 3
    cubes.append(cube)

for cube in cubes:
    print(cube)


# ----------- 4-9 Cube Comprehension -----------

cubes = [number ** 3 for number in range(1, 11)]

print(cubes)
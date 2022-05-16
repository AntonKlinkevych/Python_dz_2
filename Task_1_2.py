sum1 = 0

def sum(cube):
    num_sum = 0
    while cube != 0:
        num_sum += cube % 10
        cube = cube // 10
    return num_sum

cubes = (i**3 for i in range(1, 1000, 2))
cubes = list(cubes)
print(cubes)

for i in range(len(cubes)):
    if sum(cubes[i]) % 7 == 0:
        sum1 += cubes[i]
print(sum1)

for i in range(len(cubes)):
    if sum(cubes[i] + 17) % 7 == 0:
        sum1 += cubes[i] + 17
print(sum1)
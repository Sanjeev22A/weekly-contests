import numpy, random, math, os

def find_rotations(nums):
    return nums.index(min(nums))

limit = int(1e4)

os.makedirs("input", exist_ok=True)
os.makedirs("output", exist_ok=True)

def write(index, length, arr):
    with open(f"input/input{str(index).zfill(2)}.txt", "w") as f:
        f.write(f"{length}\n")
        f.write(" ".join(map(str, arr)) + "\n")

    result = find_rotations(arr)
    print(index, length, result)
    with open(f"output/output{str(index).zfill(2)}.txt", "w") as f:
        f.write(f"{result}\n")

for index in range(10):
    if index < 5:
        limit = 100
    else:
        limit = int(1e4)
    length = random.randint(1, limit)
    arr = numpy.random.randint(-limit, limit, size=length).tolist()
    arr = list(set(arr))
    arr.sort()
    length = len(arr)
    i = random.randint(0, length - 1)
    arr = arr[i:] + arr[:i]
    write(index, length, arr)

index = 10
length = 8
arr =  [4, 5, 6, 7, 0, 1, 2, 3]
th = 9
write(index, length, arr)

index = 11
length = 5
arr =  [3, 4, 5, 1, 2]
write(index, length, arr)

index = 12
length = limit
arr = [i - 5 for i in range(limit)]
i = random.randint(0, length - 1)
arr = arr[i:] + arr[:i]
write(index, length, arr)

index = 13
length = limit
arr = [i - 5 for i in range(limit)]
write(index, length, arr)

index = 14
length = limit
arr = [i - 5 for i in range(limit)]
i = 1
arr = arr[i:] + arr[:i]
write(index, length, arr)

index = 15
length = limit
arr = [i - 5 for i in range(limit)]
i = length - 1
arr = arr[i:] + arr[:i]
write(index, length, arr)
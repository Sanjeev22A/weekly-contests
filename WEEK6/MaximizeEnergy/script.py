import numpy, random, math, os

def getMaxBarrier(initialEnergy, th):
    def sum_after_barrier(barrier):
        return sum(max(0, e - barrier) for e in initialEnergy)
    
    low, high = 0, max(initialEnergy)
    ans = 0
    
    while low <= high:
        mid = (low + high) // 2
        if sum_after_barrier(mid) >= th:
            ans = mid      
            low = mid + 1
        else:
            high = mid - 1    
    
    return ans

limit = int(1e5)
lilimit = int(1e9)

os.makedirs("input", exist_ok=True)
os.makedirs("output", exist_ok=True)

def write(index, length, th, arr):
    with open(f"input/input{str(index).zfill(2)}.txt", "w") as f:
        f.write(f"{length} {th}\n")
        f.write(" ".join(map(str, arr)) + "\n")
        print(index, length)

    result = getMaxBarrier(arr, th)
    with open(f"output/output{str(index).zfill(2)}.txt", "w") as f:
        f.write(f"{result}\n")

for index in range(10):
    if index < 5:
        limit = 100
        lilimit = 1000
    else:
        limit = int(1e5)
        lilimit = int(1e9)
    length = random.randint(1, limit)
    th = random.randint(1, min(10000, limit))
    arr = numpy.random.randint(1, lilimit, size=length).tolist()
    write(index, length, th, arr)

index = 10
length = 5
arr = [4,8,7,1,2]
th = 9
write(index, length, th, arr)

index = 11
length = 4
arr = [5,2,13,10]
write(index, length, th, arr)

index = 12
length = limit
arr = numpy.random.randint(1, lilimit, size=length).tolist()
th = 1
write(index, length, th, arr)

index = 13
length = limit
arr = [69]*limit
th = numpy.random.randint(1, 10000)
write(index, length, th, arr)

index = 14
length = limit
arr = numpy.random.randint(1, lilimit, size=length).tolist()
th = sum(arr) - 1
write(index, length, th, arr)

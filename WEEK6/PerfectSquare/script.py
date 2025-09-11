import numpy, random, math, os

os.makedirs("input", exist_ok=True)
os.makedirs("output", exist_ok=True)

def is_square(num):
    root = int(math.isqrt(num))
    return 1 if root * root == num else 0

def write(index, n):
    with open(f"input/input{str(index).zfill(2)}.txt", "w") as f:
        f.write(f"{n}\n")

    result = is_square(n)
    print(index, n, result)
    with open(f"output/output{str(index).zfill(2)}.txt", "w") as f:
        f.write(str(result) + "\n")

for index in range(10):
    if index < 5:
        
        if index % 3 == 0:
            root = numpy.random.randint(1, 3 * int(1e3))  
            n = root * root
        else:
            n = numpy.random.randint(1, 10**6)
    else:
        
        if index % 3 == 0:
            root = numpy.random.randint(1, 4.2 * int(1e7))  
            n = root * root
        else:
            n = int(1 + numpy.random.beta(a=0.5, b=0.5) * (10**15))
    write(index, n)


index = 10
n = 16   
write(index, n)

index = 11
n = 20   
write(index, n)


index = 12
root = 10**7  
n = root * root   
write(index, n)

index = 13
n = 10**15 - 12345   
write(index, n)

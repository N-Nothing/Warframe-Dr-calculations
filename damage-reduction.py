import math

health: float = input("What is the total health value?\n")
howMany: int = input("How many DR are you stacking?\n")
print("what are they?")

DR = []

for i in range(int(howMany)):
    value = float(input())  # convert input to float
    DR.append(value)

result = [100 - dr for dr in DR]
converted = [dr / 100 for dr in result]
total = math.prod(converted)
ehp = float(health) / total

print(result)
print(converted)
print((1 - total) * 100)
print(ehp)

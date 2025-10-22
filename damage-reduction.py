import math

try:
    health: float = input("What is the total health value?\n")
except ValueError:
    print("Please enter a valid number for health.")
    exit(1)

howMany: int = input("How many DR are you stacking?\n")
print("what are they?")

DR = []

for i in range(int(howMany)):
    value = float(input())  # convert input to number
    DR.append(value)

result = [100 - dr for dr in DR]
converted = [dr / 100 for dr in result]

total = math.prod(converted)

print(result)
print(converted)
print((1 - total) * 100)
print(health / total)

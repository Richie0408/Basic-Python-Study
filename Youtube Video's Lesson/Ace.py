import random
result = 0
entity = 100
for i in range(100):
    a = random.choice(range(100))
    result += a
    print([a])
avg = result/entity
print("Total SUM: ", result)
print("Average: ", avg)



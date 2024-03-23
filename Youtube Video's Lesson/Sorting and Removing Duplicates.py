data = [10,100,90,90,80,200]
result = []
data.sort()

for i in data:
    if i not in result:
        result.append(i)

print(result)


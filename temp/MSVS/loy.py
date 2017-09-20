items = [1, 2, 3, 4, 5]
s1 = []
for i in items:
    s1.append(i**2)
    print(s1)

items = [1, 2, 3, 4, 5]
s2 = []
s2 = list(map(lambda x: x**2, items))
print(s2)

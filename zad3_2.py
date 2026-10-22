s = list()

l = int(input("Въведете дължината на списъка: "))
for i in range(l):
    s.append(int(input(f"Въведете елемент {i + 1}: ")))
print("Списъкът е:", s)

new = []
for i in range(len(s) - 1):
    new.append(s[i])
    new.append(s[i] + s[i + 1])
print("Новият списък е:", new)
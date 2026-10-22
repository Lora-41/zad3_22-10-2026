num = int(input("Въведете цяло число: "))

n = list(range(1, num + 1))

dictionary = {}

for i in range(len(n)):
    dictionary[n[i]] = n[num - 1 - i]

print(n)
print(dictionary)
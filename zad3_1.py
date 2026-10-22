number = input("Въведете число: ")

tup1 = tuple(int(x) for x in number)
tup2 = tuple(int(x) for x in number[::-1])

print("Първи кортеж:", tup1)
print("Втори кортеж:", tup2)
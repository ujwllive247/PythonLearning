x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x &= y

print(x)


x = {"a", "b", "c"}
y = {"c", "d", "e"}
z = {"f", "g", "c"}

x &= y & z

print(x)     # Only common Value..........
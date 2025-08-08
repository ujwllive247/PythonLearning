set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

JoinSet = set1.union(set2,set3,set4)       # First way.....


JoinSet = set1 | set2 | set3 | set4            # Second Way
print(JoinSet)
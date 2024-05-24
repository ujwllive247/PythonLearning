fruit = ["Orange","Apple","Banana","Papaya","Coconut"]

# for x in fruit:
#     print(x)
#     if x == "Banana":
#           break                  # Break when the item match...in the loop...


for x in fruit:
    if x == "Banana":
        continue
    print(x)               # Ignore the match value......

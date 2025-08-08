import datetime

x = datetime.datetime.now()

print(x)        #2024-05-30 18:15:49.350421


print(x.year)    #2024

print(x.strftime("%A"))       #Thursday


print(x.strftime("%B"))
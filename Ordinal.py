#This Program will loop through numbers within a list and place a string next
#Next to the number displayed.

Ord = range(1,10)

for r in Ord:
    
    if r == 1:
        print(f"{r}st")

    elif r == 2:
        print(f"{r}nd")

    elif r == 3:
        print(f"{r}rd")

    else:
        print(f"{r}th")



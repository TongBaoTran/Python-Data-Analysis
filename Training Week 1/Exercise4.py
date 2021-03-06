#Way 1: Using format syntax
i = 1
while i < 11:
    j = 1
    while j < 11:
        print("%4d" %(i*j), end=' ')   # 4d here means: the width of the integer number is fixed at 4
        j = j + 1
    print()
    i = i + 1


#Way 2: Using format method
i = 1
while i < 11:
    j = 1
    while j < 11:
        print("{:4d}" .format(i*j), end=' ')
        j = j + 1
    print()
    i = i + 1

#Way 3: Using f-string
i = 1
while i < 11:
    j = 1
    while j < 11:
        print(f"{i*j:4d}", end=' ')
        j = j + 1
    print()
    i = i + 1

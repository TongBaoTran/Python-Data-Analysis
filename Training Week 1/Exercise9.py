# help(list.append)
length1 = int(input("enter the size of list 1: "))
l1 = [0] * length1
for i in range(length1):
    l1[i] = int(input(f"L1[{i:d}]= "))
l1.sort()
print('L1: ',l1)

length2 = int(input("enter the size of list 2: "))
l2 = [0] * length2
for i in range(length2):
    l2[i] = int(input(f"L2[{i:d}]= "))
l2.sort()
print('L2: ',l2)


def merge(l1, l2):
    l = l1 + l2
    length = len(l1) + len(l2)
    swapped = True
    while swapped:
        swapped = False
        for i in range(length - 1):
            if l[i] > l[i + 1]:
                # Swap the elements
                l[i], l[i + 1] = l[i + 1], l[i]
                # Set the flag to True so we'll loop again
                swapped = True
    return l


print('sorted combined list: ',merge(l1,l2))

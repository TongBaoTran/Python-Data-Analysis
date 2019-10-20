print("Pairs that sum to 5:")
for i in range(1, 6):
    for j in range(1, 6):
        if i + j == 5:
            print("(", i, ",", j, ")")

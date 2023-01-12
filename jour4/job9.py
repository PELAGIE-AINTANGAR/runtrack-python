L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]
minimum=L[0]
maximum=L[0]
for i in L:
    if i <minimum:
        minimum=i
print(minimum)
for j in L:
    if j > maximum:
        maximum=j
print(maximum)
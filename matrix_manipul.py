initialArray = [[5,5,5,5,5,5], 
                [5,5,5,5,5,5], 
                [5,5,5,5,5,5],
                [5,5,5,5,5,5],
                [5,5,5,5,5,5],
                [5,5,5,5,5,5],
                ]

print([initialArray[i][i] for i in range(len(initialArray))])
print ([initialArray[j][len(initialArray)-j-1] for j in range(len(initialArray))])

x = [initialArray[i][i] for i in range(len(initialArray))]
for i in x:
    if i == 5:
        print("okay")
a = int(input('Enter no. of rows:'))
b = int(input('Enter no. of columns:'))

m = []

for i in range(a):
    c = []
    for j in range(b):
        j = int(input('Enter no. in Pocket ['+str(i)+'] ['+str(j)+'] '))
        c.append(j)
    m.append(c)
print('Matrix is....')
for i in range(a):
    for j in range(b):
        print(m[i][j], end=' ')
    print()
    
print(m)
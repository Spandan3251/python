table1=[1,2,3],[4,5,6]
table2=[1,2,3],[4,5,6]
print("values in table1 by row are ")
for row in table1:
    for item in row:
        print(item,end=" ")
    print()
print("values in table2 by row are ")
for row1 in table2:
    for item in row1:
        print(item,end=" ")
    print()
z=[]
for i in range(len(table1)):
        t=[]
        for j in range(len(table1[0])):
                sum=table1[i][j]+table2[i][j]
                t.append(sum)
        z.append(t)
print("added values are:")
for k in z:
    for r in k:
          print(r,end=" ")
    print()
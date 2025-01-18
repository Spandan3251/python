record=(("t1","ram","june,15,1999"),("t2","shyam","july,12,1999"),("t3","spandan","october 5,2003"))
s=input("id to fetch")
c=False
for a in range(len(record)):
    if s in record[a]:
        c=True
        break

if c==False:
    print("not found")
else:
    print("id"+"\t"+"name"+"\t"+"dob")
    for j in record[a]:
        print(j,end="\t")

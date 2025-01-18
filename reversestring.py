s=input("enter a string")
x=s.split()
r=" "
for a in x:
    r=a+" "+r
r=r.strip()
print(r)

x1=r.split()
r1=" "
for a in x1:
    r1=r1+a[::-1]+" "
r1=r1.strip()
print(r1)
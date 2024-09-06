n=int(input("\n enter any no"))
a=0
b=1
print(a)
print(b)
s=1
for i in range(3,n+1):
    c=a+b
    print(c)
    s=s+c
    a=b
    b=c
    
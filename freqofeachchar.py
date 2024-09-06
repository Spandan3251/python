s=input("\n enter a string")
x=s.split()
while x:
    c=x[0]
    n=x.count(c)
    print(c,":",n)
    x=s.replace(c,"")

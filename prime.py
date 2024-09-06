p=int(input("\n enter 1st no="))
q=int(input("\n enter 2nd no="))
for n in range(p,q+1):
    if n>1:
        f=True
        for i in range(2,n//2+1):
            if n%i==0:
                f=False
                break
        if f:
            print(n,end=" ")


s=input("\n enter name")
x=s.split()
n=len(x)
t=" "
for i in range(0,n-1):
    t=t+x[i][0]+"."
t=t+" "+x[n-1]
print("abbr",t)
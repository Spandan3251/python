s=input("\n enter a string")
if(" " in s):
    print("no space is allowed")
elif(len(s)<3 or len(s)>4):
    print("must be between 3 or 4 characters")

if (len(s)==3):
    for i in s:
        for j in s:
            if j!=i:
                for k in s:
                    if(k!=i and k!=j):
                        print(i,j,k)

if (len(s)==4):
    for i in s:
        for j in s:
            if(i!=j):
                for k in s:
                    if(k!=i and k!=j):
                        for l in s:
                            if(l!=i and l!=j and l!=k):
                                print(i,j,k,l)
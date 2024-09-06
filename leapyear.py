y=int(input("\n enter year"))
if (y%100==0):
    if(y%400==0):
        print("\n leap year")
    else:
        print("\n not leap year")
else:
    if(y%4==0):
        print("\n leap year")
    else:
        print("\n not leap year")
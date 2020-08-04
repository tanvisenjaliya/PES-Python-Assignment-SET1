a=(input("Enter the numbers:"))
b=(input())
c=input()
d=input()
greatest=0
if (a>b)&(a>c)&(a>d):
    print("the greatest no of the first 4 is",a)
    greatest=a
elif (b>a)&(b>c)&(b>d):
    print("the greatest no of the first 4 is",b)
    greatest=b
elif (c>a)&(c>b)&(c>d):
    print("the greatest no of the first 4 is",c)
    greatest=c
else:
    print("the greatest no of the first 4 is",d)
    greatest=d
e=int(input("Enter 5th number"))

if(e>int(greatest)):
    print(" The biggest of all 5 nos is",e)
else:
    print(" The biggest of all 5 nos is",greatest)

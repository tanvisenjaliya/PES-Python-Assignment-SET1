print("Enter 10 integer n: ")
sum=0
a=[]
sml=[]
for i in range(10):
    temp=int(raw_input())
    a.insert(i,temp)
for i in a:
    sum=sum+i
    print(i)
avg=sum/10
cntBig=0
cntSmall=0
cntEql=0
print("Average= ",avg)

for i in a:
    if (i<avg):
        print(i,"is smaller than avg")
        cntSmall+=1
    elif (i>avg):
        print(i, "is bigger than avg")
        cntBig+=1
    else:
        print(i, "is equal to avg")
        cntEql+=1

print("the total count of nos bigger than average is ",cntBig)
print("the total count of nos smaller than average is=",cntSmall)
print("the total count of nos equal to the average is=",cntEql)


    
      


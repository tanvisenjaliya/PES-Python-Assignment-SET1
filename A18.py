print("Printing 1 to 100 using for loop")
list1=[]
for i in range(1,101):
  print (i)
  list1.append(i)
list1.reverse()
print ("\nNumbers 1 to 100 in reverse order using the same for loop",list1)

list2=[]
i=1
print("\nPrinting 1 to 100 using while loop")
while i<=100:
  print (i)
  list2.append(i)
  i+=1
list2.reverse()
print("\nNumbers 1 to 100 in reverse order using the same while loop",list2)

mystring='Hello world'
print ("\nPrinting each character of string Hello world in separate line")
for each in mystring:
  print(each)

#a) Use membership operator ( IN ) to check the presence of an element. 
list1=['Rio','Denver','Moscow','Nairobi','Tokyo']
#print list1
if ('Rio') in list1:
  print("Rio is present in the list")
else:
  print("Rio is not present in the list")

#b) Perform above task without using membership operator. 
for i in list1:
  if (i=='Berlin'):
    print("Berlin is present in the list")
    break
else:
    print("Berlin is not present in the list")

#c) Print the elements of the list in reverse direction.
list1.reverse()
print("the elements of list1 in reverse direction are",list1)

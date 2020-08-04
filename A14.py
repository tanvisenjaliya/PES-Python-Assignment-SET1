listEId=[1,2,3,4,5,6,7,8,9,10]
listEName=['Clay','Raj','Ted','Penny','Hannah','Scheldon','Robin','Jofery','Arrya','Peter']
print ("List of Employees :",listEName)#print all the names
index=int(input("Enter the index to read from List: "))
print ("Name: ",listEName[index],"And EmpID: ",listEId[index])

print ("Names form 4-9 postion :",listEName[3:-1])
print ("Names form 3-last postion :",listEName[2:])

ntime=int(input("enter the no of times you wish to repeat the list"))
print("EmpId: ",listEId*ntime)
print ("Emp name: ", listEName*ntime)
concatList=listEId+listEName
print ("Conactnated Lists: ",concatList)
for element in range(len(listEId)):
  print ("EmpID: ",listEId[element], " EmpName: ",listEName[element])

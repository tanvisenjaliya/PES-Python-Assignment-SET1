import sys
arg1,arg2,arg3,arg4,arg5=sys.argv[0],sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4]
print ("arg1=",arg1)
print ("arg2=",arg2)
print ("arg3=",arg3)
print ("arg4=",arg4)
print ("arg5=",arg5)

arg3,arg4,arg5=input("Enter 3 numbers")
if arg3>arg4 and arg3>arg5:
  print ("the biggest no is",arg3)
elif arg4>arg3 and arg4>arg5:
  print ("the biggest no is",arg4)
else:
  print("the biggest no is",arg5)

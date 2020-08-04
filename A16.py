num=int(input("Enter the number to check for prime"))
if num==1:
  print( "Number",num,"is not a prime number")
elif num>1:
  for i in range(2,num):
    if num%i==0:
      print ("Number",num," is not a prime number")
      break
  else:
    print( "Number",num,"is a prime number")
upper=int(input("Enter the no till which you need to print the prime numbers"))
print ("The prime numbers between the given range is")
for num in range(2,upper+1):
  if num>1:
    for i in range(2,num):
      if(num%i)==0:
        break
    else:
      print (num)

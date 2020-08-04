print ("The even numbers from 1 to 100 using for loop is below:" )
for i in range(1,101):
    if i%2==0:
        print(i)
    if i==50:
        break
    if i==10 or i==20 or i==30 or i==40 or i==50:
        continue
    
    
    
print("............................")
#.a) By using For loop , use continue/ break/ pass statement to skip odd numbers.
print( "The numbers from 1 to 100 skipping odd numbers using while loop is below:" )
for i in range (1,101):
    if i%2==0:
        print (i)
    if i==90:
        break
    if i==60 or i==70 or i==80 or i==90:
        continue
  

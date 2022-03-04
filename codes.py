#whether the given number is prime number or not
''' which has two factors i.e. 1 and itself is called as the prime number '''
n=int(input("enter n:"))
fact=0
for i in range(1,n+1):
  if i%2==0:
    fact+=1
if fact==2:# the given  number has only two factors 
  print("a prime number")
else: #more than two factors or lessthan two factors
  print("Not a prime number") 
  
#Print the prime numbers in the range of 1 to 100 
n=101
for i in range(1,n):
  fact=0
  for j in range(1,i+1):
    if i%j==0:
      fact+=1
  if fact==2:
    print(i,end= " ")# hole code output in a single line
   

  
  
    

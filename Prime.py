a=int(input("Enter any number:"))
for i in range(2,a):
  if a%i==0:
    print("Not a Prime number")
    break
  else:
    print("Prime number")
else:
  print("Not a Prime number")
    

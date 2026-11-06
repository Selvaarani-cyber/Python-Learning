a=int(input("Enter any number:"))
n=a
r=0
while n>0:
  re=n%10
  r=r*10+re
  n=n//10
if n==r:
  print("Palindrome")
else:
  print("Not a Palindrome")

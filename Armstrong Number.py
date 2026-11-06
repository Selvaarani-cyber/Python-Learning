n=int(input("Enter number:"))
a=n
s=0
while n>0:
  r=n%10
  s=s+r**3
  n=n//10
if a==s:
  print("Armstrong Number")
else:
  print("Not an Armstrong Number")

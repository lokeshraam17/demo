convert=str(input("enter the type of conversion you want to perform"))
if convert=="F to C":
  F=int(input("enter value of fahrenheit"))
  print((F - 32) * 5/9,"degree celsius")
elif convert=="C to F":
  C=int(input("enter value of celsius"))
  print((C * 9/5) + 32,"degree fahrenheit")

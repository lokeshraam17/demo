print("general equation of quadratic equation is ax² + bx + c = 0")
a=(int(input("enter value for a in ax^2 ")))
b=int(input("enter value for b in bx "))
c=int(input("enter value for c in c "))
if b**2>4*a*c:
 print("root 1 =",(-b-(b**2 - 4*a*c)**0.5) / 2*a)
 print("root 2 =",(-b+(b**2 - 4*a*c)**0.5) / 2*a)
else:
 print("imaginary roots")

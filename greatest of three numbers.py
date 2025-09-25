num1=int(input("enter number 1"))
num2=int(input("enter number 2"))
num3=int(input("enter number 3"))
if num1<num2 and num2>num3:
    print(num2," is the greatest number ")
elif num2<num1 and num1>num3:
    print(num1," is the greatest number ")
else:
    print(num3," is the greatest number ")





while True:
 num1=int(input("num1:"))

 num2= int(input("num2:"))
 oper=input("enter operation:")

 if oper=="+":

  print("sum of num1 and num2 ",num1 + num2)

 elif oper=='-':

  print("difference between num1 and num2 is ",num1-num2)

 elif oper=='*':

  print("product of num1 and num2",num1*num2)

 elif oper=="/":

  print("quotient is ",num1//num2)
  print("remainder is ",num1%num2 )
operator = input("Enter The Operator(+  -  *  /): ")
num1=float(input("enter frist number 1:"))
num2=float(input("enter second num 2:"))

if operator =="+":
    result=num1 + num2
    print(round(result,3))
elif operator =="-":
    result=num1 - num2
    print(round(result,3))
elif operator =="*":
   result=num1 * num2
   print(round(result,3))
elif operator =="/":
    result=num1 / num2
    print(round(result,3))
else:
    print(f"{operator}is not valiade")



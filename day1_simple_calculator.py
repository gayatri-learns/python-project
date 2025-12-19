num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
operator=input("Enter operator(+,-,*,/,%,//,**): ")

if operator == "+": #Addition
    print("Result : ", num1+num2)
elif operator == "-": # Subtraction
    print("Result : ",num1 - num2) 
elif operator == "*": #Multiplication
    print("Result : ",num1 * num2)
elif operator == "/": #Division
    if num2 == 0:
        print("Error : Cannot Divide by ZERO")
    else:
        print("Result :",num1 / num2)
elif operator == "%": #Modulus(remainder)
    print("Result : ",num1 % num2)
elif operator == "//": #Floor division
    print("Result : ",num1 // num2)
elif operator == "**": #Power
    print("Result : ", num1 ** num2)
else: 
    print("Invalid operator")
output = 0
num1 = ""
operation = ""
num2 = ""

num1 = input("Здраствуйте, какой у вас номер?\n")
operation = input("Операция(+, -, *, /)?\n")
num2 = input("Ваш секундомер числа?\n")

floatnum1 = float(num1)
floatnum2 = float(num2)

if operation == "+":
    output=floatnum1+floatnum2
if operation == "-":
    output=floatnum1-floatnum2
if operation == "*":
    output=floatnum1*floatnum2
if operation == "/":
    output=floatnum1/floatnum2
if operation == "+" or operation == "-" or operation == "*" or operation == "/":
    print("Мой ответ! "+str(output))

else:
    print("Ваша операция, не получилось, пожалуста попробуйте сново!")












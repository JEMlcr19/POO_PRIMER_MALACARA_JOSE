num1 = int(input("Dame un numero:"))
num2 = int(input("Dame otro número: "))

if num1 > num2:
    print(num1,"Es mayor que", num2)
elif num1 < num2:
    print(num1, "Es menor que", num2)
elif num1 == num2:
    print(num1, "Y son iguales", num2)
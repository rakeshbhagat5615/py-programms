def add(x, y):
    return x + y

def sub(x, y):
    return x -y

def mul(x, y):
    return x * y

def div(x, y):
    return x / y

print("Chose choises")
print("1. Addition")
print("2. Substraction")
print("3. Multiplication")
print("4. Devision")

choise = input("Enter your choise : ")

num1 = int(input("Enter your first number : "))
num2 = int(input("Enter your second number : "))

if choise == '1':
    print(num1, "+", num2, "=", add(num1, num2))
elif choise == '2':
    print(num1, "-", num2, "=", sub(num1, num2))
elif choise == '3':
    print(num1, "*", num2, "=", mul(num1, num2))
elif choise == '4':
    print(num1, "/", num2, "=", div(num1, num2))
else:
    print("Enter valid choise")

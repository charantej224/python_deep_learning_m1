def printhelloworld():
    print('Hello World')

def addition_operation():
    return lambda num1,num2 : num1 + num2

substraction = lambda num1,num2 : num2 - num1
multiplication = lambda num1, num2 : num1 * num2
division = lambda num1, num2 : num2/num1

result = addition_operation()
print(result(10,20))

print(substraction(10,20))
print(multiplication(10,20))
print(division(10,20))
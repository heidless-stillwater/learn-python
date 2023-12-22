num1 = float(input('Enter first number: '))
op = input('Enter Operator: ')
num2 = float(input('Enter second number: '))

if op == '+':
  print('addition')
  result = num1 + num2
elif op == '-':
  print('subtraction')
  result = num1 - num2

print(result)
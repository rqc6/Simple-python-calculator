def calculate_expression(expression):
  if '+' in expression:
    numbers = expression.split('+')
    return float(numbers[0]) + float(numbers[1])
  elif '-' in expression:
    numbers = expression.split('-')
    return float(numbers[0]) - float(numbers[1])
  elif '*' in expression:
    numbers = expression.split('*')
    return float(numbers[0]) * float(numbers[1])
  elif '/' in expression:
    numbers = expression.split('/')
    if float(numbers[1]) == 0:
      return "Error: divider cannot be zero"
    return float(numbers[0]) / float(numbers[1])
  else:
    return "Invalid input"


while True:
  expression = input("Enter an operation or press Enter to quit: ")

  if expression == "":
    break

  result = calculate_expression(expression)
  print("The result of the operation is:", result)

print("Calculator closed.")

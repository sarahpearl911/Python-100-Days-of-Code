#add
def add(n1, n2):
  return n1 + n2
  
#subtract
def subtract(n1, n2):
  return n1 - n2

#multiply
def multiply(n1, n2):
  return n1 * n2

#divide
def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator():
  stop = False
  while not stop:
    num1 = float(input("What's the first number?: "))
    for symbol in operations:
      print(symbol)
    operation_symbol = input("Which operation would you like to use?: ")
    num2 = float(input("What's the second number?: "))
    
    answer = operations[operation_symbol](num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    again = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start again: ").lower()
    if again == "n":
      stop = True
      calculator()
    elif again == "y":
      stop2 = False
      while not stop2:
        operation_symbol = input("Pick another operation: ")
        num3 = float(input("What's the next number?: "))
        second_answer = operations[operation_symbol](answer, num3)
        
        print(f"{answer} {operation_symbol} {num3} = {second_answer}")
        again2 = input(f"Type 'y' to continue calculating with {second_answer}, or type 'n' to start again: ").lower()
        if again2 == "n":
          stop = True
          stop2 = True
          calculator()
        elif again2 == "y":
          answer = second_answer

calculator()

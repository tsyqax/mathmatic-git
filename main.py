def plus(a, b):
    return a + b

def minus(a, b):
    return a - b

def mega(a, b):
    return a * b

def divide(a, b):
    return a // b
  
print("계산할 숫자를 입력해주세요")
num1 = input()
print(f"{num1}인가요.. 계산 기호를 입력해주세요.")
art = input()
print("두 번째 숫자를 입력해주세요.")
num2 = input()
if art == '+':
  end = plus(num1, num2)
  pass
elif art == '-':
  end = minus(num1, num2)
  pass
elif art == 'x':
  end = mega(num1, num2)
  pass
elif art == '/':
  end = divide(num1, num2)
  pass
else:
  print("똑바로 해")
  exit()

print(end)
exit()


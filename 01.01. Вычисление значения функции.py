
from math import sqrt, cos, tan, log, sin

a = float(input('Введите значение а: '))
b = float(input('Введите значение b: '))
print()

while True:
  print()
  x = float(input('x: '))

  if x <= a:
    y = sqrt(-x) * cos(x)
  elif a < x < b:
    y = abs(tan(0.2 * x)) + x
  else:
    y = log(x) + sin(x)

  print(f'y: {y:.2f}')

# Demonstrating global variables in Python
x =66
def Show_value():
  global x
  x =36

  print(x)

Show_value()
Show_value()
Show_value()
print(x)

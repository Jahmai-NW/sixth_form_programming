 # pass multiple results back from a function
def calc(a,b):
  constantVal = 2
  x = constantVal *(a + b)
  y = a - b
  z = a * b
  return x, y, z
 
 #main program
add, subtract, multiply = calc(5,3)
print (add, subtract, multiply)
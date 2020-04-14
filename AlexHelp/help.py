import math

x = float (input("Please enter an integer "))
print(x)
print(x*x)
print(math.sqrt(x))

######################################
#   Use Mod operator instead of
#   Div to save a step
######################################
y = (x%5)
z = 0
print (y)
print (z)

#####################################
#   If/Else syntax is different than
#   C++ syntax
#
#####################################
if (y == z):
    print("The number is divisible by 5")
else:
    print("The number is not divisible by 5")
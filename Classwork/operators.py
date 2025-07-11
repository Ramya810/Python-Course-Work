#4.PythonOperators.py

#1. Arithmetic Operators

a=100
b=50

print("addition (a+b):", a+b)
print("subtraction (a-b):", a-b)
print("multiplication (a*b):", a*b)
print("division (a/b):", a/b)
print("floor division (a//b):", a//b)
print("modulus (a%b):",a%b)
print("exponentiation (a**b):", a**b)

#2. Comparison Operators

c=80
d=20

print("equal to (c==d):",c==d)
print("not equal to (c!=d):",c!=d)
print("greater than (c>d):",c>d)
print("less than (c<d):",c<d)
print("greater than or equal to (c>=d):",c>=d)
print("less than or equal to (c<=d):",c<=d)

# 3.Assignment Operator
x = 20
x += 4 
x *= 5 
x -= 50 
print(x) 

# 4.Logical Operators
x = 10
y = 20
print(x > 5 and y < 30) # Output: True (Both conditions are True)
print(x > 15 or y < 30) # Output: True (At least one condition is True)
print(not (x > 5)) # Output: False (Reverses the True condition)

#5.Membership Operators
fruits = ["apple", "banana", "cherry"]
print("apple" in fruits) # Output: True
print("grape" not in fruits) # Output: True


#6.Identity Operators
a = [1, 2, 3]
b = a
c = [1, 2, 3]
print(a is b) # Output: True (Both refer to the same object)
print(a is c) # Output: False (Different objects with the same content)
print(a is not c)

#7.Bitwise Operators
x = 5 
y = 3 
print(x & y) 
print(x | y) 
print(x ^ y) 
print(~x) 
print(x << 1) 
print(x >> 1)
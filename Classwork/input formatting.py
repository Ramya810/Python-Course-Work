#10.1 Input formatting
#1.String input
str = input("enter your name:")
print(str)

#2. integer input
int= input("enter a number:")
print(int)

#3.float oinput
flt=float(input("enter a value:"))
print(flt)

#4. input of list
n= input("Enter employee names (space-separated): ").split()
print(n)

#5. input of list (comma-seperated)
nam=input("enter a names (comma-seperated): ").split(',')
print(nam)
 
#6. list of integers
marks =list(map(int,input("Enter marks: ").split()))
print(marks)

#7. list of float
weights = list(map(float, input("Enter weights: ").split()))
print(weights)

#8. Tuple input
t=tuple(map(int, input("enter a number: ").split()))
print(t)

#9. Set input
s= tuple(map(int, input("enter a number: ").split()))
print(s)

# 10. Dictionary Input using eval()
profile=eval(input("enter a input: "))
print(profile)

# 11.Multiple Inputs with Unpacking
username, password = input("Enter username and password:").split()
print("Username:", username)
print("Password:", password)

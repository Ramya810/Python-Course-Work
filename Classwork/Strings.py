# 5.Operations on Strings
# Concatenation
str1 = "maya"
str2 = "ramya"
result = str1 + " " + str2
print(result) 

#Repetition
print("Python! " * 5) 

# Indexing
text = "Codegnan"
print(text[4]) # Output: g (5st character)
print(text[-2]) # Output: a (last 2nd character)

# Slicing
print(text[0:3])
print(text[:4]) 
print(text[2:]) 

# Membership
print('cod' in text) # Output: True
print('Java' not in text) # Output: True

#5.1 Built-in String Functions
#length
a=" ramya keshetty"
print(len(a))

#max and min
print(max("abcXYZ"))
print(min("XYZabcd"))

#Sorted (upper cases comes)
s="Hello People"
print(sorted(s))

#ord and chr
print(ord('A'))
print(chr(97))

#Case Conversion Methods
#upper() and lower()
s1="Hello People"
s2="HELLO PEOPLE"
uppercase=s1.upper()
lowercase=s1.lower()
print(uppercase)
print(lowercase)

#capitalize
capital=s1.capitalize()
print(capital)

#title
title=s1.title()
print(title)

#swapcase
swapcase=s1.swapcase()
print(swapcase)

#casefold
casefold=s1.casefold()
print(casefold)

#Alignment & Formatting Methods
#center
s3="ameerpet"
y=s3.center(20,"*")
print(y)



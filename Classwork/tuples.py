#7.1 Tuples

#syntax
tuple=()
empty_tuple=()

#indexing
t= (2,3,4,5,6,8,7)
print(t[0])
print(t[-4])
#silcing
print(t[3:7])

#1.Operations on Tuples
#a.Concatenation
t1 = (1, 2)
t2 = (3, 4)
new = t1 + t2 

#b.Repetition
tup = (1, 2)
print(tup * 3) 

#c. Membership Testing
t = (1, 2, 3)
print(2 in t) 
print(5 not in t)

#d.Tuple Unpacking
t = (1, 2, 3)
x,y,z= t
print(x,y,z)

#2.Tuple methods
#count and index
t2 = (1, 2,2,3,4,4, 3)
t1=t2.count(4)
t3=t2.index(2)
print(t1)
print(t3)

#3.Built-in Functions for Tuples
#length and max
t2 = (1, 2,2,3,4,4, 3)
l=len(t2)
m1=max(t2)
m2=min(t2)
s=sum(t2)
print(l)
print(m1)
print(m2)
print(s)

#4.Immutability and Tuple Behavior
a=([1,34],2,3)
a[0][0]=200
print(a)


e=list((1,2,3,4,5))
print(e)

#6. Lists
# creating a list

#Empty List
l=[1,2,3,4,5]
l2=type(l)
print(l2)

#contructor
c=list((1,2,3,4,5,6))
print(c)

#indexing
c=["py","th","on","start"]
print(c[0])
print(c[-2])
print(c[2])

#slicing
print(c[1:3])

#6.1 Modifying Lists
#Changing Elements
c1=[9,8,7,6,1]
c1[2]=10
print(c1)

#Adding Elements
#append
c1.append(100)
print(c1)
#insert
c1.insert(2,200)
print(c1)
#extend
c1.extend([11,22,33,44,55])
print(c1)

#Removing Elements
#remove
c1.remove(100)
#pop
c1.pop()
#pop
c1.pop(6)
#delete
del c1[2]
#clear
c1.clear()
print(c1)

#count,index,reverse,sort
numbers = [3, 1, 4, 1, 5, 9]
print(numbers.count(1)) 
print(numbers.index(4))
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)

## Shallow Copy
list = [1, 2, 3,4,5,6]
list1 = list.copy()
print(list1)

#sort and reverse
list.sort()
print(list)
list.reverse()
print(list)

#sum
l=sum(list)
print(l)
#any
l=any(list)
print(l)
#len
l=len(list)
print(l)
#all
l=all(list)
print(l)
#8.SETS
#1.syntax
set = {1, 2, 3, 4}
print(set)

# 2.Set Properties
'''set = {[1, 2], 3}
print(set)'''

#3. Operations on Sets
#a. Membership Testing
a={2,3,4,5,6,7,8}
print(8 in a)
print(12 not in a)

# b.Union (| or union() method
set1={2,3,4,5,6}
set2={0,9,5,4,2}
print(set1|set2)

# c.intersection
print(set1&set2)

# d.Difference
print(set1-set2)

# e.Symmetric Difference
print(set1^set2)

# f.Subset
print(set1<=set2)

# g.Superset
print(set1>=set2)

#h. Disjoint Sets
print(set1.isdisjoint(set2))

# 4.Built-in Methods for Sets
set = {1, 2, 3, 4}
set.add(5)
set.remove(4)
set.discard(1)
set.pop()
print(set)
set1={2,3,4,5,6}
set2={0,9,5,4,2}
print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))
print(set1.symmetric_difference(set2))
print(set1.update(set2))

#5.Built-in Functions for Sets
sets={1,2,3,14,15,6,7,18,9,10,100}
print(len(sets))
print(max(sets))
print(min(sets))
print(sum(sets))
print(sorted(sets))

#6. Frozensets
frozen = frozenset([1, 2, 3])
print(frozen)

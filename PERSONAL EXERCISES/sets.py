set1={"aaaa", "bbbb", "cccc", "aaaa", "dddd"}
set2={1,2,3,4,5,6}
set3={True,False,False,True,False}
set4={True,1,False,"abbb",4,"school"}
set5=set(("a","b","c","d","f"))

set1.add("ffff")	# Add “x” to the set.

set2.update(set1) # Add all elements of sequence “s” to the set.

set3.remove(True)	# Remove “x” from the set. If “x” is not present, this method raises a LookupError exception.

set4.discard(4)	# Remove “x” from the set if it is present, or do nothing if it is not---

set1.pop()	# Remove and return an arbitrary element, raising a LookupError if the element is not present.-----

#set2.clear()	# Remove all elements from this set.

set3.copy() # 	Make a new set

x=set4.issuperset(set3) # Check for a superset relationship.

y=set1.issubset(set2)	# Check for a subset relationship.

#set()	# Cxreate a set containing the elements of the collection “x”.

z= frozenset(set2) # Create an immutable set containing the elements of the collection “x”.'''
print(z)
print(y)
print(set1)
print(set2)
print(set3)
print(set4)
print(set5)
print(type(set1))
print(len(set4))
print(set5)
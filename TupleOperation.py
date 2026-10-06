tuple=(17.2526 , 74.5025)
print(tuple)

# Accessing of element 
print(tuple[0])

#Accessing of last element
print(tuple[-1])

#slicing
print(tuple[0:1])
print(tuple[0:2])

#Concatination
tuple1=(1.108 , 2.116)
concatination=tuple + tuple1
print(concatination)

#Multiplication
mul=tuple*2
print(mul)

#Searching
print(17.2526 in tuple)

#Length
print(len(tuple))

#Count
print(tuple.count(17.2526))

#Indexing
print(tuple.index(17.2526))
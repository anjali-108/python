list=[1,2,"Anjali","Shinde",3]
print(list)

#Accessing the element
print(list[1])

#updating element
list[1]=8
print(list)

#adding element of the list
list.append(6)
print(list)

list.append("Sakshi")
print(list)

#insert method
list.insert(4,5)
print(list)

#extend
list.extend([4,3])
print(list)

#removing element
list.remove(1)
print(list)

#pop method
list.pop(4)
print(list)

#del keyword
del list[3]
print(list)

#length of the list
print(len(list))

#in keyword
if 8 in list:
    print("Element is present ")
else:
    print("Element is absent")

#list traversal
for i in list:
    print(i)    

#count
print(list.count(8))

#index method
print(list.index(6))

#reverse method
list.reverse()
print(list)

list2=[90,50,60,30,10]

#sort list
print(list2.sort())  #asending order
print(list2)

print(list2.sort(reverse=True))      #desending order
print(list2)

#copy method
newlist=list.copy()
print(newlist)

#clear method                                                                                                                                  
list.clear()
print(list)
list1=[12,-7,5,64,-14]
print(list1)
for n in list1:
    if n>0:
        print(n ,end=" ")
    list2=[12,14,-95,3]
print("\n" ,list2)
y=list(filter(lambda x:(x>=0),list2))
print(y)
        
    

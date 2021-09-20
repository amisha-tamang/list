
# DIFFERENCE


list1 = [1,2,3,4,5,6]
list2 = [2,3,1,0,6,7]
i=0
k=[]
while i <len(list1):
    a=list1[i]
    if a not in list2:
        k.append(a)
    i=i+1
print(k)           
    

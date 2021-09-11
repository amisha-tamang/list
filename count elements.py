
# COUNT ELEMENTS


elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43] 
i=0
a=[]
b=[]
count=0
count1=0
while i<len(elements):             
    j=elements[i]
    if j%2==0:
        a.append(j)
        count=count+1
    else:
        b.append(j)
        count1=count1+1
    i=i+1   
print("total elements=",i)    
print("even number=",count)
print("odd number=",count1)

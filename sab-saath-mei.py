
# SAB SAATH MEI

elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43] 
i=0
a=[]
b=[]
sum=0
sum1=0
sum2=0
avg=0
count=0
count1=0
while i<len(elements):
    h=len(elements)          
    j=elements[i]
    if j%2==0:
        a.append(j)
        sum=sum+j
        sum2=sum1+sum+j+1
        count=count+1
    else:
        b.append(j)
        sum1=sum1+j 
        count1=count1+1
    i=i+1
avg=sum/4
avg1=sum/7   
avg2=sum/11 
print("total even=",count)
print("total odd=",count1)
print("total element",h)
print("odd sum=",sum1)
print("even sum=",sum)
print("total element sum=",sum2)
print("even number",a)
print("odd number",b)
print("even average=",avg)
print("odd average=",avg1)
print("elements average",avg2)



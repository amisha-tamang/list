numbers = [50, 40, 23, 70, 56, 12, 5, 10, 7] 
max=numbers[0]
i=0
while i<len(numbers):
    # num=numbers[i]
    if numbers[i]>max:
      max=numbers[i]
    i=i+1
print("frist max:- ",max)      
max2=numbers[0]      
j=0
while j<len(numbers):
    if numbers[j]>max2:
        if numbers[j] != max:
            max2=numbers[j]
    j=j+1
print("second max:- ",max2)
max3=numbers[0]
k=0
while k<len(numbers):
    if numbers[k] >max2 and max3:
        if numbers[k] != max and max2:
            max3=numbers[k]
    k+=1
print("thrid max:- ",max3)

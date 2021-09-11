
# Yeh pichle saat dinon mein temperatures ki list hai.

# temperature_list=[21.1, 24.3, 19, 25, 17, 18, 23]
# print(temperature_list) 


numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7] 
i=0
count=0
m=[]
while i<len(numbers):
    if numbers[i]>20 and numbers[i]<40:
        m.append(numbers[i])
        count=count+1
    i=i+1
print("count","=",count,m)    

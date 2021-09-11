

# List Iteration - Question

  # Code likho jo di gayi list mein jo number 20 se bade hai aur
  #  40 se chote hai unhe count kare. Aur firr unka count print kare.


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






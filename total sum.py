# TOTAL SUM

number=30
n=[10, 11, 12, 13, 14, 17, 18, 19] 
i=0
a=[]
while i<len(n):
    j=len(n)-1
    while j>4:
        if n[i]+n[j]==number:
            a.append([n[i],n[j]])
        j=j-1
    i=i+1
print(a)           
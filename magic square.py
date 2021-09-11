# MAGIC SQUARE 

magic_square = [
    [8, 3, 4],
    [1, 5, 9],
    [6, 7, 2]
]
i=0
a=[]
rowsum=0
while i<len(magic_square):
    j=magic_square[i]
    if j:
        a.append(j)
        rowsum=rowsum+1
    i=i+1
    a=a+1   
print(rowsum)
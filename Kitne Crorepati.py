
#  KITNE CROREPATI

kitna_paisa_hai=[3000, 600000, 324990909, 90990900, 30000, 5600000, 690909090, 31010101, 532010, 510, 4100] 
Crorepati=[]
Lakhpati=[] 
Dilwale=[]
i=0
while i<len(kitna_paisa_hai):
    if kitna_paisa_hai[i]>=10000000:
        Crorepati.append(kitna_paisa_hai[i])
    elif kitna_paisa_hai[i]>=100000:
        Lakhpati.append(kitna_paisa_hai[i])
    else:
        Dilwale.append(kitna_paisa_hai[i])
    i=i+1
print("crorepati hai",Crorepati)
print("lahkhpati hai", Lakhpati)
print("dilwale hai",Dilwale)


# line="metazone: the happy world"
# num=line.split(" ",0)
# print(num)




# o/p= the quick brown fox jumped the lazy dog. the dog slept the verandah. 
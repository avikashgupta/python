***There is an array of n integers. There are also 2 disjoint sets,  and , each containing m integers. You like all the integers in set A and dislike all the integers in set B. 
Your initial happiness is . For each  integer i in the array, if i belongs to A , you add 1 to your happiness. If i belongs to B , you add  -1 to your happiness. 
Otherwise, your happiness does not change. Output your final happiness at the end.***

def sets_logic():
    e = True
    
    while(e):
        b = set(map(int,input().split()))
        if len(b)==m:
            break 
        else:
            b = set(map(int,input().split()))
    return b


n, m = map(int, input().split())

r = True
while(r):
    a = list(map(int,input().split()))
    if len(a)==n:
        break 
    else:
        a = list(map(int,input().split()))



set1 = sets_logic()
set2 = sets_logic()

if set1.isdisjoint(set2)==True:
    pass
else:
    print()
    print()
    for i in range(2):
        sets_logic()


happiness = 0

for i in a:
    if i in set1 and i not in set2:
        happiness+=1
    if i in set2 and i not in set1:
        happiness-=1

print(happiness)

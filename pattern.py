odd = True
while(odd):
    thickness = int(input()) #This must be an odd number
    if (thickness%2!=0 and 2<=thickness<=50):
        odd = False
    else:
        odd = True
    
c = '#'

#Top Cone
for i in range(thickness):
    print((c*(i+1)+c*i).center(thickness*2))

#Top Pillars
for i in range(thickness):
    print((c*thickness).center(thickness*2)+(c*thickness).rjust((thickness*2)*2))
    
#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*6).center(thickness))
    
#Bottom Pillars
for i in range(thickness):
    print((c*thickness).center(thickness*2)+(c*thickness).rjust((thickness*2)*2))
    

#Bottom Cone
for i in range(thickness-1,0,-1):
    print((c*(i+1)+c*i).center(thickness*2))
    if i==1:
        print(c.center(thickness*2))

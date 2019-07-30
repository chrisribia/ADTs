lst = [7, 6, 4, -1, 1, 2]
sum = 16
def quads(lst,sum)
for i in lst:
    for x in lst:
        for w in lst:
             for p in lst:
                 sum = i + x + w +p
                 if sum == 16:
                      print(i,x,w,p)

            
       

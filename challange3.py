Array_A = [5, 10, 20, 28, 3,875875]
Array_B = [85721,26, 134, 135,8523252, 15,8888, 173456787]

min = Array_A[0] - Array_B[0] 
for i in Array_A:
    for n in Array_B:
        dif = i - n 
        dif2 = n - 1
        if dif < dif2:
            while min > dif: 
                min = dif
                print(i,n,dif)
        else:
            while min > dif2: 
                min = dif2
                print(i,n,dif2)


        

def sum_two(lst):
    """
    ARGS:
        function takes list as argument

    Returns:
        returns a list of two numbers of sum 10  

    Run Time:
        
    """   
    lst = sorted(lst) #time = 1
    
    min = lst[0]#time = 1
    for i in lst[1:]:#time = n
        sum = min + i#time = 1
        for x in lst:#time = n
            sum2 = x + sum#time = 1
            if sum2 == 0:#time = 1
                print(min,i,x,)


"""total time 1 +3n*n""
    total time n*n
"""
sum_two([12, 3, 1, 2, -6, 5, -8, 6] )
                


 
 
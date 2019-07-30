lst = [12, 3, 1, 2, -6, 5, -8, 6]
def sum_two(lst,sum):
    """
    ARGS:
        function takes list as argument

    Returns:
        returns a list of two numbers of sum 10  

    Run Time:
        O(n)
 
    """
    triplets = [] 
    for i in lst:
        for x in lst:
            sum2 = i + x
            if sum2 < sum:
                triplets.append(i)
                triplets.append(x)
                third_number = sum - sum2
                if third_number in lst and third_number not in triplets:                    
                    triplets.append(third_number)                    
                    print(triplets)
                     
                
sum_two(lst,0)

  

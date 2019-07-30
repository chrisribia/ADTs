lst = [3, 5, -4, 8, 11, 1, -1, 6] 
def sum_two(lst,sum):
    """
    ARGS:
        function takes list as argument

    Returns:
        returns a list of two numbers of sum 10  

    Run Time:
        O(n)

    """
    n = {x:sum-x for x in lst 
                        if (sum - x) in lst  and (x - sum) in lst}
    print(n)

sum_two(lst,sum = 10)
 
 
 


    
     
 

class setAdt:
    """implementing  set adt"""


    def __init__(self,myset):
        """initializing my set adt"""
        self.myset = []
        

    def add_item(self,item):
        """adding item to my set
         Run Time:
            constant time : o(1).
        
        """
        return self.myset.append(item) 


    def remove_item(self,index):
        """removing an item from the set
        
        Run Time:
            Linear time : o(n).
        """
        return self.myset.pop(index)
        
 
    def check_item(self,item):
        """checking if an item is in set
        
        Run Time:
            Linear time : o(n).
        """
        for i in self.myset:
            if i == item:
                return "item exist in the set"
         
        
    def union_of_sets(self,set2):
        """find the union of two sets
         Run Time:
            constant time : o(1).
        """
        for i in set2:
            if i not in self.myset:
                self.myset.append(i)
        return self.myset
         
        
    def sets_intersection(self,set2):
        """return the itersection of two sets
        
        Run Time:
            Linear time : o(n).
        """
        itersection_set = []
        for i in set2:
            if i   in self.myset:
                itersection_set.append(i)
        return itersection_set
        

    def set_diffrence(self,set2):
        """return the difrence between two sets
        
        Run Time:
            Linear time : o(n).
        """ 
        set_diffrence = []
        for i in set2:
            if i  not in self.myset:
                set_diffrence.append(i)
        return set_diffrence

    def symetric_diffrence(self,set2):
        """return symytric diffrence
          Run Time:
            constant time : o(1).
        """ 
        union_results = self.union_of_sets(set2)
        inter_section = self.sets_intersection(set2)

        sym_diff = []

        for i in union_results:
            if i not in inter_section:
                sym_diff.append(i)

        return sym_diff   

      
    def set_subset(self,set2):
        """return the if set is subset of another
          Run Time:
            constant time : o(1).
        """
        my_intersetion = self.sets_intersection(set2)
        if len(my_intersetion) == len(set2):
            return True
        else:
            return False

class map_adt:
    def __init__(self,map_adt):
        """implementing map using list """
        self.map_adt = []

    def add_dict(self,*dictionaries):
        """add dict to dictionary
         Run Time:
            linear time : o(n). 
        """
        return self.map_adt.append(dictionaries)

    def get_all_items(self):
        """get all items in the mapping
         Run Time:
            linear time : o(n). 
        """
        for item in self.map_adt:
            return item

    def get_specific_dict(self,dict_key):
        """returning a dictionary Run Time:
                    linear time : o(1). 
        """
        return self.map_adt[dict_key]


    def get_element_of_spec_dict(self,dict_key,element_index):
        """get an element from dict using its index
         Run Time:
            linear time : o(n). 
        """      
        
        answer = self.get_specific_dict(dict_key)
        if answer != "":
            return answer[element_index]
        else:
            raise Exception("No value")

    def update_value(self,dict_key,element_index,new_value):
        """update an element of dictionary
         Run Time:
            linear time : o(1). 
        """ 
        answer = self.get_specific_dict(dict_key)
        if answer != "":
            new_answer =  answer[element_index] = new_value
            return new_answer
        else:
            raise Exception("No value")




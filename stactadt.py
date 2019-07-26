class Stack:
    def __init__(self):
        """initalizing empty stack"""
        
        self.stack_adt = []

    def length(self):
        """ getting the length of stack
        time = O(n)
        """

        return len(self.stack_adt)

    def is_empty(self):
        """check if stack is empty
        time = O(1)
        """

        if self.length == 0:
            return True
        else:
            return False

    def add_item(self,item):
        """add item to a stack
          Constant time: O(1)
        """
        return self.stack_adt.append(item)

    
    def remove_item(self):
        """remove last element from stack
         Time:
            constant time: O(1)  
        """

        if self.is_empty:
            raise Exception("stack is Empty")
        else:
            return self.stack_adt.pop()

    def peek(self):
        """return top item from a stack        
        Time : O(1)
        """
        if self.is_empty:
            raise Exception("stack is Empty")
        else:
            return self.stack_adt[:-1]

class LinkedStack:
    class _Node:
        """create a node"""
        def __init__(self,element,next):
            self.element = element
            self.next = next

    def __init__(self):
        """contents of the node"""
        self.head = None
        self.size = 0

    def len(self):
        """return the size of stackRun 
        Time:
                   constant time : o(1)
        """
        return self.size

    def is_empty(self):
        """check if stack is empty
        Run Time:
            constant time : o(1)
        """
        return self.size == 0

    def push(self,element):
        """add a node to the stack
        Run Time:
            constant time : o(1)
        """
        self.head = self._Node(element,self.head)
        self.size +=1

    def peek(self):
        """return element at the top of the stack
        Run Time:
            constant time : o(1)
        """
        if self.is_empty:
            raise Exception("Stack is Empty")
        else:
            return self.head.element
    def pop(self):
        """remove the top node of the stack
        Run Time:
            constant time : o(1)
        """
        if self.is_empty:
            return Exception("Stack is empty")
        answer = self.head.element
        self.head = self.head.next
        self.size -=1
        return answer

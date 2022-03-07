from exceptions import EmptyStackException, NullElementException

class Stack:
    """
        Basic Stack implementation for testing purposes
    """
    def __init__(self, *initial_data):
        self.__stack = list(initial_data)
        pass

    def size(self):
        return len(self.__stack)

    def push(self, element):
        if element is None:
            raise NullElementException()
        self.__stack.append(element)


    def pop(self):
        if len(self.__stack) == 0:
            raise EmptyStackException()
        
        return self.__stack.pop()

    def peek(self):
        if len(self.__stack) == 0:
            raise EmptyStackException()
        return self.__stack[-1]
    
    def empty(self):
        return len(self.__stack) == 0


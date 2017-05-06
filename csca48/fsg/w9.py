''' Abstract data types
ADT: Independant of implementation
-user doesnt need to know (or care) how ADT works
- Should in theory be able to write code without a class having been
implemented yet
- Does it do this? Does it do that? Don't know, don't care
- for our purposes, and ADT is just the documentation of the class,
before we've written the implementation
Design -> Document -> Comment -> Code
UML: Unified Modelling Language
Stacks: are LIFO(Last In First Out)
Queue: are FIFO(First In First Out)
'''
class EmptyStackError(Exception):
    ''' raise an error'''


class Stack():
    '''A LIFO stack of objects'''

    def __init__(self):
        '''(Stack) -> NoneType
        '''
        self._contents = {}
        self._height = 0

    def push(self, new_item):
        '''(Stack, object) -> NoneType
        Add new_item to the top of the stock
        '''
        self._contents[self._height] = new_item
        self._height += 1


    def pop(self):
        '''(Stack) -> object
        Remove and return the top item from the stack
        RAISES: StackEmptyError if the stack is empty
        '''
        self._height -= 1
        if(self._height < 0):
            raise EmptyStackError("You can't pop from an empty stack")
        else:
            return_item = self._contents[self._height]
        return return_item

    def is_empty(self):
        '''(Stack) -> bool
        Return True iff the stack is empty
        '''
        return (len(self._contents) == 0)

######################

if(__name__ == '__main__'):
    my_stack = Stack()
    my_stack.push('A')
    my_stack.push('B')
    my_stack.push('C')
    print(my_stack.pop())
    my_stack.push('D')
    for count in range(5):
        try:
            print(my_stack.pop())
        except EmptyStackError:
            print("oops, tried to pop too many times")
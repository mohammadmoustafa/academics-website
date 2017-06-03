class LLNode():

    def __init__(self, data, next_ptr=None, prev_ptr=None):
        '''(self, object, LLNode, LLNode) -> NoneType
        '''
        # initiate our node with the private variables data and ptr
        # if the user doesnt want to pass in a a pointer, we use None as
        # a default value
        self.data = data
        self.prev = prev_ptr
        self.next = next_ptr

    def __str__(self):
        # return the Node's data in the following format
        return 'Node({}, {})'.format(str(self.data), str(self.next))

    #def get_data(self):
        # return the data container in self._data
        #return self._data

    #def set_next(self, new_ptr):
        # change what the node points to
        # change the pointer from ptr to new_ptr
        #self._ptr = new_next

    #def set_data(self, new_data):
        # change the data stored in the node from data to new_data
        #self._data = new_data

if __name__ == "__main__":
    a = LLNode(1)
    b = LLNode(2)
    c = LLNode(3)
    a.next = b
    b.prev = a
    print(a)
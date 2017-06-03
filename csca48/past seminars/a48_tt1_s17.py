from containers import *

def size(stk):
    """(Stack) -> int
    Return the number of items on Stack stk, *without* modifying stk.
    (It’s OK if the contents of stk are modified during the execution of this
    function, as long as everything is restored before the function returns.)
    """
    # Hint: you can use more than one stack
    copy = Stack()
    count = 0
    while not (stk.is_empty()):
        copy.push(stk.pop())
        count += 1

    while not copy.is_empty():
        stk.push(copy.pop())

    return count


def reverse ( head ) :
    """ ( LLNode ) -> LLNode
    Given the head pointer to a linked list ,
    reverse the linked list and return a pointer
    to the head of the reversed list .)
    """
    current = head
    previous = None
    while current :
        next = current . next
        current . next = previous
        previous = current
        current = next
    head = previous
    return head
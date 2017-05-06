'''
CSCA48 TT2 Seminar, March 10th 2017

Yufei Cui & Brian Chen
AMACSS
'''


'''
Notes:
1) please change the multiple return statements into one return statement
only.

2) add proper docstring (i.e. type contract, REQ, examples, etc)

3) PEP8
'''

def merge(a,b):
    '''
    Given 2 sorted lists a, b and returns a sorted list combining the elements from a and b
    '''
    # if a is empty
    if not a:
        return b
    # if b is empty
    elif not b:
        return a
    # recursion step
    else:
        # find the smallest value in both lists
        if l1[0] < l2[0]:
            # put the smallest element in the front and recursively sort the rest
            return [l1[0]] + merge(a[1:],b)
        else:
            return [l2[0]] + merge(a, b[1:])

def edit_distance(s1, s2):
    ''' The edit distance of two strings is defined as: The minimum number of single character changes that would be needed to turn s1 into s2.
    Easy: assume that s1 and s2 are the same length, and the only character changes available are replacing one character with another.'''

    # base case, empty string
    if len(s1) == 0:
        return 0
    # recursion step
    else:
        # if the elements at index 0 is the same
        if s1[0] == s2[0]:
            # check all other chars
            return edit_distance(s1[1:], s2[1:])
        else:
            # check all othe chars + 1 (because the chars at index 0 is diff)
            return 1 + edit_distance(s1[1:], s2[1:])


#print(edit_distance("",""))
#print(edit_distance("Hello","World"))
#print(edit_distance("Jenkin","Jenkun"))

def edit_distance2(s1, s2):
    '''
    Hard: assume s1 and s2 may be different lengths, and we can also add and delete characters.'''

    # if s1 is empty
    if not s1:
        return len(s2)
    # if s2 is empty
    elif not s2:
        return len(s1)
    # recursion step
    else:
        # return the minimum of deleting both 0th element, deleting the s1's 0th element, and deleting s2's 0th element
        return min((edit_distance2(s1[1:],s2[1:]) + (s1[0] != s2[0])), edit_distance2(s1[1:],s2)+1, edit_distance2(s1,s2[1:])+1)

def subsequence(s1, s2):
    '''
    s1 is a subsequence of s2 iff s2 can be made equal to s1 by removing 0 or more of its characters. Example:
    subsequence(’dog’,’XYZdABCo123g!!!’) should return True.
    Easy: Return True iff s1 is a subsequence of s2.
    '''
    # base cases
    if s1 == s2:
        return True
    # if s1 is empty, all empty strings are subsequences of all other strings
    elif not s1:
        return True
    # if s1 is longer than s2, s1 cannot possibly be substring of s2
    elif len(s1) > len(s2):
        return False
    # recursion step
    else:
        # check the chars at first index
        if s1[0] == s2[0]:
            # recursively call the rest of the 2 strings
            return subsequence(s1[1:],s2[1:])
        else:
            # otherwise, remove that char from s2 and recursively call the rest
            return subsequence(s1,s2[1:])

def perms(s):
    '''
    Easy: Given a string s, return a set of all possible permutations of the letters in s.
    '''
    # initialize a return set
    ret = set()
    # base cases: if s is empty
    if not s:
        return ret
    # if s is only a char
    if len(s) == 1:
        return set(s)
    # recursion step
    else:
        # return the permutated list of a smaller string namely, s w/o the first char
        permed = perms(s[1:])
        # for every element in the set
        for elmt in permed:
            # here I want to loop through all the possible index from 0 to len(elmt) + 1
            for i in range(len(elmt)+1):
                # insert s[0] in between all possible indices i
                new_s = elmt[:i] + s[0] + elmt[i:]
                # add the element into the set
                ret.add(new_s)
        return ret
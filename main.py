"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.

def foo(x):
    if x <= 1: # if x is less than or equal to 1, return x
        return x
    else: # else recursively go through x and return the sum of (x-1) + (x-2)
        return(foo(x-1)+foo(x-2))
   # pass

def longest_run(mylist, key):
    mylength = 0 
    maximum_length = 0 

    for number in mylist: 
        if number == key: 
            mylength += 1 
            maximum_length = max(mylength, maximum_length) 
        else: 
            mylength = 0 
    return maximum_length 
# this code will create 2 integer values to store the current length of the longest key sequence (mylength) and the maximum length of the longest key sequence (maximum_length). Then, it will iterate through our list of numbers (mylist), and add 1 to mylength each time the key is found, and 0 if the key is not found. At the end, the maximum length is returned.


class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size               # run on left side of input
        self.right_size = right_size             # run on right side of input
        self.longest_size = longest_size         # longest run in input
        self.is_entire_range = is_entire_range   # True if the entire input matches the key
        
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))
    

def to_value(v):
    """
    if it is a Result object, return longest_size.
    else return v
    """
    if type(v) == Result:
        return v.longest_size
    else:
        return int(v)
        
def longest_run_recursive(mylist, key):
    # base case for empty list
    if len(mylist) == 0:
        return Result(0,0,0,True)
    #base case for list of size 1, where the item is the key
    elif len(mylist) == 1:
        if mylist[0] == key:
            return Result(1,1,1,True)
        # base case for list of size 1, where the item is not the key
        else:
            return Result(0,0,0,False)

    
    else:
        # if the list has more than 1 item, we will split the list in half and recursively find the longest sequence
        middle = len(mylist)//2 # split in half
        left = longest_run_recursive(mylist[:middle], key) 
        right = longest_run_recursive(mylist[middle:], key) 
        mylength = 0

        # new cases depending on which side contains the value & how many 

        # CASE 1: Left side of mid is entirely the value but left is not
        if left.is_entire_range and not right.is_entire_range:
            mylength = left.longest_size
            return Result(left.longest_size + right.left_size, right.right_size, max(left.longest_size + right.left_size, right.longest_size), False)

        # CASE 2: Right side of mid is entirely the value but right is not
        if right.is_entire_range and not left.is_entire_range:
            mylength = right.longest_size
            return Result(left.left_size, right.longest_size + left.right_size, max(left.right_size + right.longest_size, left.longest_size), False)

        # CASE 3: Both sides of mid are entirely the value
        if left.is_entire_range and right.is_entire_range:
            mylength = left.longest_size + right.longest_size
            return Result(left.longest_size + right.longest_size, left.longest_size + right.longest_size, left.longest_size + right.longest_size, True)

        # CASE 4: Neither side of mid is entirely the value
        else:
            return Result(left.left_size, right.right_size, max(left.longest_size, right.longest_size, left.right_size + right.left_size), False)

            

        
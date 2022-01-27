"""Project 6.1: Binary Search
    Author: Danny Harris
    Description: This project will take a sorted list (alist)
    and will search for a target value within that list by
    means of Iteration and Recursion.
    If the target value exists in the list, the function will
    return True. Otherwise, the function will return False.

    Note: I realize that I could condense my conditional statements
    into something more concise, but considering the function I have
    written at the very bottom, is_member(), is a much more
    efficient and effective way of reaching the same goal, so I figure
    cleanliness is not of much importance with this project.

    """
def is_memberI(alist, target):
    """(list, int) -> Boolean

    This function will take a sorted list (alist) and will iterate
    through the values within. It will do so with respect to the
    median of the values in comparison to the target value (target).
    Function will return True if target exists/occurs within alist,
    otherwise it will return False.

    >>> is_memberI([1, 3, 5, 7], 4)
    False
    >>> is_memberI([23, 24, 25, 26, 27], 5)
    False
    >>> is_memberI([0, 1, 4, 5, 6, 8], 4)
    True
    >>> is_memberI([0, 1, 2, 3, 4, 5, 6], 3)
    True
    >>> is_memberI([1, 3], 1)
    True
    >>> is_memberI([2, 10], 10)
    True
    >>> is_memberI([99, 100], 101)
    False
    >>> is_memberI([42], 42)
    True
    >>> is_memberI([43], 44)
    False
    >>> is_memberI([], 3)
    False
    """
    alist.sort() #Just in case you feel like throwing in an unordered list.
    if len(alist)%2 == 0:
        high = len(alist)//2
        low = high - 1
        if len(alist) == 0:
            return False
        elif target > alist[-1] or target < alist[0]:
            return False
        elif target < alist[low]:
            counter = 0
            while len(alist[:(low - counter) + 1]) >= 0:
                if target == alist[counter]:
                    return True
                    break
                else:
                    counter += 1
                    if len(alist[:(low - counter)]) == 0:
                        return False
        elif target > alist[high]:
            counter = 0
            while len(alist[(high + counter):]) > 0:
                if target == alist[(high + counter)]:
                    return True
                    break
                else:
                    counter += 1
                    if len(alist[(high + counter):]) == 0:
                        return False
        elif target == alist[low]:
            return True
        elif target == alist[high]:
            return True
        else:
            return False
    elif len(alist)%2 != 0:
        median = len(alist)//2
        if target < alist[0] or target > alist[-1]:
            return False
        elif target < alist[median]:
            counter = 0
            while len(alist[:(median - counter)]) > 0:
                if target == alist[counter]:
                    return True
                    break
                else:
                    counter += 1
                    if len(alist[:(median - counter)]) == 0:
                        return False
        elif target == alist[median]:
            return True
        else:
            counter = 0
            while len(alist[(median + counter):]) > 0:
                if target == alist[(median + counter)]:
                    return True
                    break
                else:
                    counter += 1
                    if len(alist[(median + counter):]) == 0:
                        return False

def is_memberR(alist, target):
    """(list, int) -> Boolean

    This function will take a sorted list (alist) and will recursively
    check the values within. It will search for a target value by first
    checking if alist is an empty list, if not, it will check if the last
    item in the list is the target value. Otherwise, the function will
    call itself on alist.pop(), searching for the target value in alist
    without the last item in the list.
    Function will return True if target exists/occurs within alist,
    otherwise it will return False.

    >>> is_memberI([1, 3, 5, 7], 4)
    False
    >>> is_memberI([23, 24, 25, 26, 27], 5)
    False
    >>> is_memberI([0, 1, 4, 5, 6, 8], 4)
    True
    >>> is_memberI([0, 1, 2, 3, 4, 5, 6], 3)
    True
    >>> is_memberI([1, 3], 1)
    True
    >>> is_memberI([2, 10], 10)
    True
    >>> is_memberI([99, 100], 101)
    False
    >>> is_memberI([42], 42)
    True
    >>> is_memberI([43], 44)
    False
    >>> is_memberI([], 3)
    False
    """
    if len(alist) == 0:
        return False
    elif target == alist[-1]:
        return True
    else:
        alist.pop()
        return is_memberR(alist, target)
        

def is_member(alist, target):
    """(list, int) -> Boolean

    The much cleaner, more effective and efficient form of
    this function.
    Returns True if a sorted list (alist) contains value (target).
    Returns False otherwise.

    >>> is_member([1, 3, 5, 7], 4)
    False
    >>> is_member([23, 24, 25, 26, 27], 5)
    False
    >>> is_member([0, 1, 4, 5, 6, 8], 4)
    True
    >>> is_member([0, 1, 2, 3, 4, 5, 6], 3)
    True
    >>> is_member([1, 3], 1)
    True
    >>> is_member([2, 10], 10)
    True
    >>> is_member([99, 100], 101)
    False
    >>> is_member([42], 42)
    True
    >>> is_member([43], 44)
    False
    >>> is_member([], 3)
    False
    """
    if target in alist:
        return True
    else:
        return False
    

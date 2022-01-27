"""Project 8: Counting Majors
    Authors: Danny Harris and Thomas Michiels
    Description: This project will take a file
    of listed majors and report the frequency
    of each major, and the most frequently occuring
    major in the file.
    """

def mean(alist):
    """(list) -> float

    Function takes a list parameter (alist) and
    returns the mean value as a float.

    >>> mean([1, 2, 3, 4, 5])
    3.0
    >>> mean([1, 2, 3, 4])
    2.5
    """
    mean = sum(alist)/len(alist)
    return mean

def frequencyTable(alist):
    """(list) -> None

    Calls: genFrequencyTable

    Function takes a list and calculates the
    frequency of the occurrances of each value
    within the list.
    Function prints values from the list in a
    table with the number of occurrances.
    Function returns None.

    >>> frequencyTable([1, 2, 3, 4, 1, 2, 3, 4])
    1   2
    2   2
    3   2
    4   2
    >>> frequencyTable([1, 3, 5, 2, 6, 3, 7, 0, 7, 9, 9, 7, 5])
    0   1
    1   1
    2   1
    3   2
    5   2
    6   1
    7   3
    9   2
    """
    dictionary = genFrequencyTable(alist)
    blist = list(dictionary.keys())
    blist.sort()
    for i in blist:
        print(i, " ", dictionary[i])

def genFrequencyTable(alist):
    """(list) -> dict

    Function will take a list and calculate
    the frequency of each value within the list.
    Dictionary keys will be items from alist,
    dictionary values will be the frequency.
    Function returns dictionary.

    >>> genFrequencyTable([1, 2, 3, 4, 1, 2, 3, 4])
    {1: 2, 2: 2, 3: 2, 4: 2}
    >>> genFrequencyTable([1, 1, 1, 3, 4, 7])
    {1: 3, 3: 1, 4: 1, 7: 1}
    """
    dictionary = {}

    for i in alist:
        if i in dictionary:
            dictionary[i] = dictionary[i] + 1
        else:
            dictionary[i] = 1
    return dictionary

def mode(alist):
    """(list) -> list

    Calls: genFrequencyTable

    Function takes a list of the values from the
    dictionary returned by the function genFrequencyTable,
    and finds the greatest value in that list, essentially
    finding the most occuring item in alist.
    If the value associated with a key in the dictionary
    is equal to the maxcount, then that is the mode.
    The mode is returned within a list.

    >>> mode([1, 2, 2, 3])
    [2]
    >>> mode(["CIS", "HIST", "CIS", "CIS"])
    ["CIS"]
    >>> mode([1, 2, 3, 4])
    [1, 2, 3, 4]
    """
    genFrequencyTable(alist)
    countlist = genFrequencyTable(alist).values()
    maxcount = max(countlist)

    modelist = []
    for i in genFrequencyTable(alist):
        if genFrequencyTable(alist)[i] == maxcount:
            modelist.append(i)
    return modelist

def majors_main():
    '''() -> None

    Calls:  majorsf_to_li, report

    Top level function for analysis of
    data in file of majors of students
    in CIS 210 W16.

    Access major file, create list
    of relevant data, and report the mode
    and frequency table for the data in the file.

    Returns None.

    >>> majors_main()
    '''
    
    with open('majors_CIS210_W16.txt', 'r') as majorsf:
        
        majorsli = majorsf_to_li(majorsf)
        majorsli.remove("Major")    #This removes the title of the list "Major"
    report(majorsli)

    return None

def majorsf_to_li(majorsf):
    """(file) -> list

    Function takes an opened file (majorsf)
    and reads it, splitting each line such
    that each line is a new element in a list
    (majorsli).
    Function returns majorsli.

    >>> majorsf_to_li("majors_CIS_W16.txt")
    (list consisting of each line in the parameter file)
    """
    majorsli = majorsf.read().splitlines()
    return majorsli

def report(alist):
    """(list) -> None

    Calls: mode, frequencyTable

    Function takes a list (alist), which in
    this case is the list generated from the
    function majorsf_to_li, and prints the most
    frequently occuring item, and prints the
    parameter list in a frequencty table format.
    Function returns None.

    >>> report(["CIS", "HIST", "CIS"])
    CIS   2
    HIST   1
    """
    print(mode(alist))
    frequencyTable(alist)
    return None

def median(alist):
    """(list) -> float

    Function will calculate the median value of a
    list.
    Function returns floating point number.

    >>> median([1, 3, 5, 7])
    4.0
    >>> median([1, 3, 5, 7, 9])
    5.0
    """
    alist.sort()
    if len(alist)%2 == 0:
        high = len(alist)//2
        low = high - 1
        median = float((alist[high] + alist[low])/2)
        return median
    else:
        median = len(alist)//2
        return float(alist[median])

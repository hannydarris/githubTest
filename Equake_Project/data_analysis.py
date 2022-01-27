"""Project 6.2: Data Analysis
    Author: Danny Harris
    Description: This project will create a graph
    based on the frequency of occurrances of values
    within a list parameter. Turtle graphics, lists,
    and dictionaries will be used in this exercise.

    Note: I did not include the earthquake data list
    in my docstrings so as to keep my docstrings to
    a minimum.
    """
import turtle

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

def frequencyTable(alist):
    """(list) -> None

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

def frequencyChart(alist):
    """(list) -> None

    Function takes a list of values, counts the
    frequency of each value within the list, and
    creates a graph using turtle graphics.
    Function returns None.

    >>> frequencyChart([1, 2, 3, 4, 1, 2, 3, 4])

    >>> frequencyChart([1, 3, 5, 2, 6, 3, 7, 0, 7, 9, 9, 7, 5])
    
    """
    newDict = genFrequencyTable(alist)
    itemL = list(newDict.keys())
    mini = 0
    maxi = len(itemL)-1
    defsL = list(newDict.values())
    maxD = max(defsL)

    turtle.setworldcoordinates(-1, -1, maxi + 1, maxD + 1)
    turtle.hideturtle()
    turtle.up()
    turtle.goto(0, 0)
    turtle.pd()
    turtle.goto(maxi, 0)
    turtle.up()
    turtle.goto(-1, 0)
    turtle.write("0", font=("Helvetica", 16, "bold"))
    turtle.goto(-1, maxD)
    turtle.write(str(maxD), font=("Helvetica", 16, "bold"))
    
    for i in range(len(itemL)):
        turtle.goto(i, -1)
        turtle.write(str(itemL[i]), font=("Helvetica", 16, "bold"))
        turtle.goto(i, 0)
        turtle.pd()
        turtle.goto(i, newDict[itemL[i]])
        turtle.up()
    turtle.Screen().exitonclick()

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
    

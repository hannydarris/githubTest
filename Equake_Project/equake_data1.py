"""Project 9.1: Earthquake Data Analysis
    Authors: Danny Harris and Thomas Michiels
    Description: This project takes earthquake magnitude
    data from a website, and reports the mean, median, and mode
    of such data, and generates a frequency table from it.

"""

import urllib.request
import data_analysis_more as d

def equake_main():
    """() -> None
    Calls: readeqf, equake_analysis
    
    Top level function for analysis of
    earthquake data from USGS website.

    Returns None.

    >>> equake_main()
    """
    emags = readeqf()
    equake_analysis(emags)
    return None

def readeqf():
    """() -> list

    Function requests and opens url and returns
    a list of the magnitudes of the earthquakes
    given in the data on that page.

    >>>readeqf()
    [5.2, 5.1, 5.0, 5.7, 5.8, 5.4, 5.3, 5.4, 5.2, 5.6]
    """
    eList = []
    page = urllib.request.urlopen("http://earthquake.usgs.gov/fdsnws/event/1/query?format=csv&starttime=1916-02-01&latitude=44.0519&longitude=-123.0867&maxradiuskm=250&minmagnitude=5")
    for i in page:
        line = i.decode()
        line = line.rstrip().split(',')

        if len(line) > 1:
            eList.append(line[4])
    del eList[0]
    eList = [float(i) for i in eList]

    page.close()
    return eList
    

def equake_analysis(mags):
    """(list) -> None
    Calls: readeqf, frequencyTable, mean, median, mode

    Function calculates and prints mean, median, and mode
    of a list parameter (mags) as well as a frequency table.
    Function returns None.

    >>> equake_analysis(readeqf())
    prints(Mean: 5.37 
    Median: 5.35 
    Mode: [5.4, 5.2] 
    Magnitude: Frequency:
    5.0   1
    5.1   1
    5.2   2
    5.3   1
    5.4   2
    5.6   1
    5.7   1
    5.8   1)
    """
    print("Mean:", d.mean(mags), "\n"
          "Median:", d.median(mags), "\n"
          "Mode:", d.mode(mags), "\n"
          "Magnitude:", "Frequency:")
    d.frequencyTable(mags)
    return None

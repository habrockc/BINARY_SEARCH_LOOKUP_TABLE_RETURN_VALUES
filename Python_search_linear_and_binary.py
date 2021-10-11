# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 16:31:43 2020

@author: cdhabro
"""

import pandas as pd
import numpy as np
import datetime


np.random.seed = 42


"""
length = 15

letterWord = ['abcdefghijklmnopqrstuvwxyz'*length]
letterString = letterWord[0]
letters = list(letterString[0:length])



df = pd.DataFrame({"DATE" : pd.date_range("1/1/2020", periods=length, freq="D"),
                   "VALUE": np.random.randint(0, length, size=length),
                   "CAT" : letters
                   })


dfSAV = df.sort_values(by=["VALUE"], ascending=True)

search = dfSAV["VALUE"].values
print(search, "\n", type(search))
### if using binary search, use set(<input array>) to get unique values


look = 8
landscape = search
"""



# fake data for when what temperatures in Fahrenheit feel like
df = pd.DataFrame({"TEMP_FEELS":["FREEZING", "CHILLY", "WARM", "HOT", "SIZZLING"],
                   "TEMP":[32, 50, 65, 80, 100]})

# resorting to make input not sorted before being searched
df = df.sort_values(by=["TEMP_FEELS"], ascending=True).reset_index(drop=True)
dfSAV = df.sort_values(by=["TEMP"], ascending=True)

search = dfSAV["TEMP"].values
print(search, "\n", type(search))







### so far, function version 3 seems to be working, need tighter QC. Also need 
### figure out when toFind is > or < than anything in findUniverse




def chooseClosestAbsVal(target, val1, val2):
    """Find closest value to target by taking absolute value difference of val1 and val2)
    Requires three parameters:
    target is value: (int or float);
    val1 and val2: (int or float)
    """
    val1Abs = abs(target - val1)
    val2Abs = abs(target - val2)
    
    print(f"Finding closest match of {(val1, val2)} to {target}")
    print(f"Absolute value of val1: {val1Abs}")
    print(f"Absolute value of val2: {val2Abs}")
    if val1Abs < val2Abs:
        closestAbsResult = val1
    elif val1Abs > val2Abs:
        closestAbsResult = val2
    elif val1Abs == val2Abs:
        print(f"Absolute value differences are equal, returning previous index.")
        closestAbsResult = np.min([val1, val2])    
    print(f"Closest absolute value: {closestAbsResult}")
    return closestAbsResult






tstart = datetime.datetime.now()




def binary_Search(toFind, findUniverse, closeMatch=None):
    """Look for 'toFind' in 'findUniverse'.
    Requires two parameters:
    toFind is value to look for: (int or str);
    findUniverse are items to search: (list of int or str);
    closeMatch: default is None, can be 'previous' or 'next'
    """
    
    
    if closeMatch in [None, "previous", "next", "closest"]:
        #print("closeMatch is valid")
        pass
    else:
        raise Exception("closeMatch parameter is invalid")
    
    
    # test if findUniverse contains strings
    stringExists = any([isinstance(check, (str)) for check in findUniverse])
    print(f"String exists: {stringExists}")
    
    if stringExists == True:
        findUniverse = [stringUpper.upper() for stringUpper in findUniverse]
        #print(findUniverse)
        #print()
        
        toFind = toFind.upper()
        print(f"Looking for {toFind} in {findUniverse[0:10]}")
    
    
    tF = toFind
    findUniverseSorted = sorted(findUniverse, reverse=False)
    
    
    print("Sorting list in ascending order:")
    print(findUniverseSorted[0:5])
    print()
    
    
    """
    ### new dev 1/20/2021
    if toFind < min(findUniverseSorted):
        if 
    
    
    ### end dev 1/20/2021
    """
    
    
    searchCounter = 0
    initialHigh = len(findUniverseSorted)

    low = 0
    high = initialHigh - 1
    mid = 0

    print(f"---SEARCHING FOR {tF:}---")
    print(f"***INITAL search: find {tF:} among {(initialHigh):,} items***")
    print()

    # test if first item in sorted array is what we are searching for
    if findUniverseSorted[low] == tF:
        print(f"FOUND {tF} ON FIRST TRY!")
        print()
        return mid

    # item searching for is not the first item in array, continue searching
    while low <= high:
        searchCounter += 1
        
        mid = (low + high) // 2
        
        print()
        print(f"---SEARCHING FOR {tF:}---")
        print(f"Search #: {searchCounter:,}")
        print(f"# items searched: {((high-low) + 1):,} of {initialHigh:,}")
        print(f"search low index: {low:,}")
        print(f"search mid index: {mid:,}")
        print(f"search high index: {high:,}")
        print()
                       
            
        if findUniverseSorted[mid] < tF:
            low = mid + 1
            print(f"{tF:} is right of value at index: {mid:,}")
            closestSmallestIdx = mid
            print(f"We would keep {findUniverseSorted[closestSmallestIdx]} as closest value less than searched")
            print()
        elif findUniverseSorted[mid] > tF:
            high = mid - 1
            print(f"{tF:} is left of value at index: {mid:,}")
            closestSmallestIdx = mid - 1
            print(f"We would keep {findUniverseSorted[closestSmallestIdx]} as closest value less than searched")
            print()
        else:
            #print(f"Search iterations: {searchCounter:,}")
            #print(f"FOUND {tF:}, located at index position: {mid:,}")
            return mid
        
  
    #print(f"low: {low} {findUniverseSorted[low]}, mid: {mid} {findUniverseSorted[mid]}, high: {high} {findUniverseSorted[high]})")
    #return None
    #return np.min([low, mid, high])
    returnOptions = [low, mid, high]
    itemBeforeIdx = np.min(returnOptions)
    itemAfterIdx = np.max(returnOptions)
    
    itemBeforeValue = findUniverseSorted[itemBeforeIdx]
    itemAfterValue = findUniverseSorted[itemAfterIdx]
    
    if closeMatch == None:
        print(f"NONE: {tF:} is not in search items")
        print(f"Search iterations: {searchCounter:,}") 
        return None
    elif closeMatch == "previous":
        #itemBefore = np.min(returnOptions)
        print(f"NONE: {tF:} is not in search items but {findUniverseSorted[itemBeforeIdx]} is item before {tF}.")
        return itemBeforeIdx
    elif closeMatch == "next":
        #itemAfter = np.max(returnOptions)
        print(f"NONE: {tF:} is not in search items but {findUniverseSorted[itemAfterIdx]} is item after {tF}.")
        return itemAfterIdx        
    elif closeMatch == "closest":
        closestAbsValue = chooseClosestAbsVal(tF, itemBeforeValue, itemAfterValue)
        print(f"Closest abs val: {closestAbsValue}")
        #itemBeforeValue = findUniverseSorted[]
        if closestAbsValue == itemBeforeValue:
            closestAbsIdx = itemBeforeIdx
        elif closestAbsValue == itemAfterValue:
            closestAbsIdx = itemAfterIdx
        print(f"Closest abs value: {closestAbsValue} found at index: {closestAbsIdx}")
        return closestAbsIdx
    
    #     closestValue = np.min(np.abs(tf - findUniverseSorted[np.min(returnOptions)]), abs(tf - findUniverseSorted[np.max(returnOptions)]) )
    #     return closest
    # firstless return np.min(returnOptions)
    else: 
        return None

binary_Search(5, sorted(np.arange(0,31, 7), reverse=True), closeMatch="closest")
#firstSearchGreaterBinary(5555, set(np.random.randint(50, high=10000, size=100)) )
#firstSearchGreaterBinary(6231, s)

tend = datetime.datetime.now()
print()
print(f"Execuction time: {tend - tstart}")





### datasets to play with ###
forms = pd.DataFrame({"Depth":[0, 2500, 5000, 10000], "Zone":["shallow", "lower", "middle", "deep"], "Temp":[100,115,175,250]})

for n in np.arange(498, 502):
    z = binary_Search(n, forms["Depth"], closeMatch="previous")
    print()
    print(f"Depth entered: {n}     Zone: {forms.loc[z, ['Zone']]}")
    print()


### create dataframe containing values that we need to assign formation names
dummyRowSize = 20
dummyCol = np.random.randint(10002, size=dummyRowSize)
dummyDf = pd.DataFrame({"DEPTHS_TO_ASSIGN": dummyCol})

# use dataframe column with values to search and apply binary_Search algorithm to return indices
## two lines below are duplicates but with different parameter for 'closeMatch') 
#dummyDf["matched_index"] = dummyDf["DEPTHS_TO_ASSIGN"].apply(lambda x: binary_Search(x, findUniverse=forms["Depth"], closeMatch=None))
dummyDf["matched_index"] = dummyDf["DEPTHS_TO_ASSIGN"].apply(lambda x: binary_Search(x, findUniverse=forms["Depth"], closeMatch="previous"))
# use matched index to map value from another column
dummyDf["matched Zone"] = dummyDf["matched_index"].map(forms["Zone"])
dummyDf["matched Temp"] = dummyDf["matched_index"].map(forms["Temp"])
print()
print("-"*100)
print(dummyDf)
print()
print("-"*50)
print(forms)
print()
print()

### showing all search methods from a loop of match options

fours = np.arange(1,100,9)

resultDict = {}

for match in [None, 'previous','next','closest']:
    tempBS = binary_Search(0, fours, closeMatch=match)
    resultDict[match] = tempBS
print()
print()
print("RESULTS")
for k, v in resultDict.items():
    print(f"{k}: {v}")


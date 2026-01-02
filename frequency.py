def findFrequency(arr, k):      #function define
    hm = dict()                #create empty dict

    for val in arr:            #loop through the list
        hm[val] = hm.get(val,0) + 1      #if val already exist in the dict ---> return its value  , if val does not exist reyurn 0

    if k in hm:               #check if k exists
        return hm[k]
    else:
        return 0

arr = [0, 5, 5, 5, 4]
k = 5

print(findFrequency(arr, k)) #calls the function findFrequency
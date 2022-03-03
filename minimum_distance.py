arr = [1,4,2,3,2,6,4,3,1] 
#          ^   ^           returns: 2

arr2 = [1,2,3,4,5,6,7,8,9]  # returns -1

'''
the numbers are saved in the form of a dictionary where the numbers are keys and their indexes are a list of values
ex:
{
1:[0,8],
2:[2,4], ..
}
the initial minimum distance will be the length of the array + 1 (will be our distinctive condition in case there are no reoccuring numbers)
than we loop throught the elements of each list, substracting consecutive indexes and saving the minimum value, than returning it.
if the minimum value is the initial value (an impossible distance) that means that there are no reoccuring numbers, returning -1.
'''

def min_distance(arr):
    # initiate dictionary of frequent numbers
    dcc = {}                       
    # intitate the minimum distance
    mind= len(arr)+1
    for index, number in enumerate(arr):
        if number in dcc.keys():
            dcc[number].append(index)
        else:
            dcc[number] = [index]
    for key in dcc:          
        for i in range(1, len( dcc[key])):
            if mind > dcc[key][i]-dcc[key][i-1]:
                mind = dcc[key][i]-dcc[key][i-1]
    return mind if mind != len(arr) else -1
    
print(min_distance(arr2))
print(min_distance(arr))

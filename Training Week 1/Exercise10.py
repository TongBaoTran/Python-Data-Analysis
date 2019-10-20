import itertools

"""
def detect_ranges(ilist):
    sorted_list = sorted(set(ilist))
    range_start = sorted_list[0]   
    range_end=sorted_list[0]
    for number in sorted_list[1:]: 
        if number == range_end + 1: 
            range_end = number 
        else: 
            yield (range_start, range_end) 
            range_start = range_end=number
    yield (range_start, range_end)
  
# Driver code 
l = [2,5,4,8,12,6,7,10,13]
print( list(detect_ranges(l)))
""" 
    
    
def detect_ranges(ilist):
    iterable = sorted(set(ilist)) 
    for key, group in itertools.groupby(enumerate(iterable), lambda t: t[1] - t[0]): 
        group = list(group)
        if group[0][1]== group[-1][1]:
            yield group[0][1]
        else:
            yield (group[0][1], group[-1][1])

# Driver code 
l = [2,5,4,8,12,6,7,10,13]
print(list(detect_ranges(l)))
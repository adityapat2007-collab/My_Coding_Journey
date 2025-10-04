# important note: in both generating subsets and permutations, we assume elements are in a consecutive sequence

import itertools # or can import permutations directly from itertools
arr = [1,2,3]
# most efficient way in python:
result = list(itertools.permutations(arr,len(arr))) # if import permutations, permutations(arr)
# here the second argument (r) is the length of permutations you want
print(result)
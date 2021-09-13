"""
proble statement:
The longest increasing subsequence (LIS) problem is:
• Input: a nonempty list of integers.
• Output: the length of its longest subsequence that is weakly increasing

eg: 1) input : 1,2,3,4,5,6,7,8
       output: 1,2,3,4,5,6,7,8.
    2) input : 1, 5, 6, 3, 4, 8
       output:1, 3, 4, 8 with a length of 4 elements.
"""


"""
Algorithm 1 Longest Increasing Subsequence
    1: Input: List A of integers, length n.
    2: Create array L and set L[1] = 1.
    3: for j = 2, . . . , n do
    4:  Set L[j] = 1.
    5:  for i = 1, . . . , j − 1 do
    6:      if A[i] ≤ A[j] and L[j] < L[i] + 1 then
    7:          Set L[j] = L[i] + 1.
    8:      end if
    9:  end for
    10: end for
    11: Return maxj L[j]"""
    
def __LongestIncreasingSubsequence__(input_array):
    L = []
    previous_selection = []
    max = 1
    for j in input_array:
        L[j] = 1
        for i in j-1:
            if input_array[i] <= input_array[j] and L[j] < L[j] + 1:
                L[j] = L[i] +1
                if max < L[j]:
                    max = L[j]    
    print("Length of longest increasing sequence:" + max)
    print("Runnig time for this algorithm is O(n^2)")


def __main__ ():
    print("this is main")



__main__()
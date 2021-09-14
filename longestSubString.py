"""Longest Common Substringproblem, the input consists of two strings,XandY. 
 Theoutput should be the length of the longest string that is a substring of bothXandY.
 A  substring  must  be  consecutive.   
 For  example,  ifX=ALGORIT HMandY=RHY T HM, 
 thenT HMis a substring of both, butRT HMis not a substring of either (eventhough it is a “subsequence”).
"""


def __longestSubSrtring__(string1, string2):

    max = 0
    max_i = 0
    max_j =0
    C = [[0 for i in range(0, len(string2)+1)] for j in range(0, len(string1)+1)]
    for i in range(0, len(string1)):
     
        for j in range(0, len(string2)):
            
            if (i == 0 | j == 0):
                C[i][j] = 0
            elif string1[i] == string2[j]:
                C[i][j] = C[i-1][j-1] +1
                if(max < C[i][j]):
                    max = C[i][j]
                    max_i = i
                    max_j =j
            else:
                
                C[i][j] = 0
    print("Length of Longest sub string is :", max)
    print("Longest sub string is:", end=" ")
    temp_max_i = max_i - max +1
    while C[max_i][max_j] >0:
        #print("temp i is ",temp_max_i)
        print( string1[temp_max_i], end=" ")
        max_i = max_i -1
        max_j = max_j -1
        temp_max_i = temp_max_i +1
            

    
def __main__ ():
    string1 = 'ALGORITHM'
    string2 = 'RHYTHM'
    
    __longestSubSrtring__(string1, string2)
    



__main__()
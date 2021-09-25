"""
The edit distance between two strings (i.e. lists of characters) is the smallest number of transformations 
needed to convert one string into the other. The allowable transformations are:
• Substitute one character for any character. • Insert a new character anywhere.
• Delete any existing character.
Note this is symmetric: If we can get from string X to Y in a series of transformations, 
we can get back in the same number of steps by reversing them.


"""

def edit_distance(string1, string2):
    E = [[0 for i in range(0, len(string1)+1)] for j in range(0, len(string2)+1)]
    for i in range(0,len(string2) + 1):
        E[i][0] = i # for the all deletion case.
    
    for j in range(0,len(string1) + 1):
        E[0][j] = j  # for all insertion case.
    
    
    for i in range(1,len(string2) + 1):
        for j in range(1,len(string1) + 1):
            a = E[i-1][j] + 1
            b = E[i][j-1] + 1
            if (string2[i-1] == string1[j-1]):
                c = E[i-1][j-1]
            else :
                c = E[i-1][j-1] + 1
            E[i][j] = min(a,b,c)
    

    print(E[len(string2)][len(string1)])
    

def __main__():
    string1 = "HELLO"
    string2 =  "HELL"
    
    edit_distance(string1, string2)
__main__()
            

    
"""You are a cashier whose goal is to give customers their correct change while using asfew total coins as possible.  
The input is the set of available coin denominations as integersx1, . . . , xn; 
and the amount of change that is due, an integer W. 
The output is the fewestnumber of total coins that add up to W.
"""
import array as arr


def __coinDenomination_greedy__ (denomination, w):
    print ("Input\n \tdenominations" + str(denomination) + "weight: " + str(w)  )
    #sort coin denominations
    denomination.sort(reverse = True)
    print(denomination)
    count =  0
    frequency = {}
    #Keep subtracting the larget denominations which satisfies the condition w[i] < remaining weight
    for i in denomination:
        count = count + w//i
        frequency[i] = w//i
        w = w%i
    print(count)
    #print the number of coins used per denominaiton
    print(frequency)



def __coinDenomination_dynamic__ (denomination, w): 
    print ("Input\n \tDenominations:" + str(denomination) + "Weight: " + str(w))
    #W[0] =0
    weight = [0]*(w+ 1)
    trace = [0]*(w+ 1)
    weight[0] = 0
    for i  in range(1,w+1):
        min_denominations = 99999
        trace[i] = 0


        for j in denomination:
            if (i - j >=0):
                if (min_denominations > weight[i-j]):
                    min_denominations = weight[i-j] + 1
                    trace[i] = j 

        if (min_denominations == 99999):
            weight[i] = 99999
        else :
            weight[i] = min_denominations 
    print("total coins used :",weight[w])
    i = w
    while trace[i] !=0:
        print (trace[i], end= " ")
        i = i - trace[i]
  






def __main__ ():
    print("this is main")
    denomination1 = [1,7,15,33,51,99]
    denomination2 = [1, 5, 10, 25, 50, 100]
    weight1 = 72
    weight2 = 2919
    
    #Greedy
    __coinDenomination_greedy__(denomination1, weight1)
    __coinDenomination_greedy__(denomination1, weight2)
    __coinDenomination_greedy__(denomination2, weight1)
    __coinDenomination_greedy__(denomination2, weight2)

    #using dynamic solution approch
    __coinDenomination_dynamic__(denomination1, weight1)
    __coinDenomination_dynamic__(denomination1, weight2)
    __coinDenomination_dynamic__(denomination2, weight1)
    __coinDenomination_dynamic__(denomination2, weight2)



__main__()
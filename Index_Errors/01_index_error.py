import math
import os
import sys
import re
import random

if __name__ == '__main__':
    n = int(input().strip())


# step-1 :- so there are 2 categories "weird" and "not weird" hence if and else will be used here
# step-2 :- cases for "weird" ;- n is odd, n is even with [6,20] both inclusive
#step-3 :- cases for "not weird" :- n is even and >20, n is even and in [2,5] inclusive

# constraint ------ 1<= n <= 100
#means that the for 1 its weird,
#               for 2  its not weird,
#               for 3 its weird,
#               for 4 its not weird,
#               for 5 its weird,    
#                for 6,8,10,12,14,16,18,20 its weird,  
# #               for 7,9,11,13,15,17,19 its weird,      
#                 for even no. from 21 till 100 its not weird.
#               for rest odd greater than 20 its  weird

    if n%2 == 1:
        print("Weird")

    elif n%2 == 0 and 2 <= n <= 5:
        print("Not Weird")

    elif n%2 == 0 and 6<= n <= 20:
        print("Weird")

    elif n%2 == 0 and 20< n <= 100:
        print("Not Weird")
""" pattern.py pseudo code
using if-else and a for loop (preferrably one)
create
1 *
2 **
3 ***
4 ****
5 *****
6 ****
7 ***
8 **
9 *

count up from 1-5
count down from 5-8
"""

star = "*"
for num in range(1,11): # creating the range from 0 skipped the first line
    if num <= 5: # raises the number of stars up until the 5th line
        pattern = num * star 
        print(pattern)

    else: # for remaining iterations of loop
        pattern = (10 - num) * star
        print(pattern)
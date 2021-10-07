"""
Bhavya stands in a line of M people, but is not sure about the position he occupies.
He is sure that there are no more than Y people behind him and no less than X people in front of him. 
Find the number of different positions Bhavya can occupy.

Sample input 1  - 3 1 1 
Sample output 1 - 2
Sample input 2 - 5 2 3
Sample output 2 - 3

"""
M,Y,X= map(int,input().split())
no_of_pos=0
i=0
j=M

while 0<=i<=Y and X<=j<=M:
    i+=1
    j-+1
    no_of_pos+=1

print(no_of_pos)
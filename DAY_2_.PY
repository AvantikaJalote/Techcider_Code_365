""" 
Day 2 - 
A floor has a center wooden section of size ‘n×m’, that has to be covered with carpet. 
The carpet has to be stitched using square pieces of cloth of length ‘a’.
Find the minimum number of cloths that must be stitched together to cover the wooden section. 
The carpet may cover an additional area outside the wooden floor. 
The input contains 3 integers, n m a, in the respective order. 

Sample Input 1: 6 6 4
Output 1: 4 pieces

Sample input 2: 8 10 3
Output 2 : 12 pieces

"""
n,m,a= map(int,input().split())

i=int(n/a)
j=int(m/a)

if(i*a!=n):
    i+=1
if(j*a!=m):
    j+=1

print(i*j)
def isRectangle(a, b, c, d):

    if (a==b and d==c) or (a==c and b==d) or (a==d and b==c):
        return True
    else:    
        return False
 
 
a, b, c, d = map(int, input().split())

flag=isRectangle(a,b,c,d)
if flag==True:
    print("\nThe sides form a rectangle")
else:
     print("\nThe sides don't form a rectangle")
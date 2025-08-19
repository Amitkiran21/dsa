# expression 1
"""def exp1(n):
    sum = 0
    for i in range(n+1):
        sum += i**2
        print(sum)
    print(sum)
n = int(input("enter:"))
exp1(n)"""

# expression 2
"""def exp2(n):
    sum = 0
    for i in range(n+1):
        sum += i**i
        print(sum)
    print(sum)
n = int (input("enter:"))
exp2(n)"""

#expression 3
# pattern i
"""n = 5
for i in range(n):
    for j in range(n):
        print('*' , end=" ")
    print()"""
# pattern a
"""n = 5
for i in range(n):
    for j in range(n):
        if (j<=i):
            print ('*',end=" ")
    print()"""
#pattern d
"""n = 5
for i in range(5,0,-1):
    for j in range(5,0,-1):
        if (j <=i):
            print('*', end=" ")
    print()"""
#pattern g
"""n = 5
for i in range(n):
    for j in range(i,n):
        print ('',end=" ")
    for j in range (i+1):
        print('*', end=" ")

    print()"""

# pattern b
"""n = 5
for i in range(n):
    for j in range(i,n):
        print (' ',end=' ')
    for j in range (i+1):
        print('*', end=' ')

    print()"""

# pattern e
"""n = 5
for i in range(n+1):
    for j in range (n+1):
        if (j<=i):
            print(' ',end =' ')
        else:
            print('*', end =' ')
    print()"""

# pattern c
"""n=7
for i in range (n):
    for j in range (n):
        if (j == n//2 or i ==n//2):
            print ('*', end=' ')
        else:
            print (' ',end=' ')
    print()"""
# pattern f
"""n=7
for i in range (n):
    for j in range (n):
        if ( i==j or i+j+1==n ):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()"""

# pattern h (create (a) with spaces and d,e with stars)
"""n = 5
for i in range(n):
    for j in range (i+1):
        print('', end =" ")
    for j in range (i,n-1):
        print('*',end="")
    for j in range (i,n):
        print('*',end="")
    print() """
# HOLLOW patterns 
# j
"""n = 5
for i in range(n):
    for j in range (i,n+1):
        if (i == 0 , j ==i , j== n-1):
            print('*',end=" ")
        else:
            print(' ',end=" ")
    print()"""

# k
#l 
"""n = 5
for i in range(n):
    for j in range (n):
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            print('*', end = ' ')
        else:
            print(' ', end = ' ')
    print ()"""




        
    
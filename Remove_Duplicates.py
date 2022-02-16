'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

Define a Python function remdup(l) that takes a nonempty list of integers l and removes all duplicates in l, keeping only the first occurrence of each number. For instance:

''' 
def remdup(l):
    v = []
    if len(l)!=0:
        for i in l:
            if i not in v:
                v.append(i)
    
    return v

print(remdup([3,1,3,5]))

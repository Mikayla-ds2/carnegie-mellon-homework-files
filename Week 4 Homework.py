#Week 4 Optional Homework
#Eucledian Algorithm
def eucledianAlgorithm(a,b):
    r = 1
    lst = [] #remainder list
    multiple = 1 
    while r != 0:
        multiple = findMultiple(a,b) 
        r = b - multiple
        lst.append(r)
        a,b = r, a
        
    print('gcd(a,b) =',lst[-2])
        
        
def findMultiple(a,b):
    factor = 1
    multiple = 1
    if b % a == 0:
        multiple = b
    else: 
        while (a * factor) <= b:
           multiple = a * factor
           factor += 1
    return multiple



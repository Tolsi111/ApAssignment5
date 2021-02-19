'''
In this module you will find some usefull functions for the problem
'''
def switch(a,b):
    '''
    switches the values of the parameters "a" and "b"
    '''
    #print(a,b,"\n")
    aux = a
    a = b
    b = aux
    #print(a,b,"\n")

def validIndex(l,i):
    '''
    Forces the user to input a valid index "i" for the list "l"
    '''
    while True:
        if i.isnumeric():
            if 0 <= int(i) and int(i) < len(l):
                break
        i = input("invalid index, please insert a valid index: ")
    return int(i)
    
def validNumber(x):
    '''
    Forces the user to insert a number
    '''
    while not x.isnumeric() and not x[1:].isnumeric():
        x = input("please insert a number: ")
    return int(x)

def positiveNumber(x):
    '''
    Forces the user to insert a positive number
    '''
    while x <= 0:
        x = input("please insert a number >0 : ")
    return x


def mySort(lst,relation):
    '''
    Bubble sort
    '''
    Sorted = False
    t = 0
    while not Sorted:
        Sorted = True
        for i in range(1,len(lst)-t):
            if not relation(lst[i-1],lst[i]):

                aux = lst[i-1]
                lst[i-1] = lst[i]
                lst[i] = aux

                Sorted = False
        t += 1
    return lst

def mySearch(lst,condition,param):
    '''
    This function searches and returns a list of all the elements from "lst" that satisfy the "condition"
    "condition" is a function that returns true or false
    For this particular problem, a 3rd parameter "param" is required

    '''
    result = []
    for elem in lst:
        if condition(elem,param):
            #print(elem)
            result.append(elem)
            #print("\n")
    return result

def first3Digits(a):
    '''
    This function returns the first 3 digits of an int
    '''
    while a > 1000:
        a = a // 10
    return a

def isThreeDigits(x):
    '''
    Checks if 'x' is a 3-digit positive number
    '''
    if 99 < x and x < 1000:
        return True
    return False
#BACKTRACKING ALGORITHM
def init(domain):
    '''
    Function that generates an empty value for the definition domain of the solution
    '''
    return -1
def isSolution(solution, k):#condition for it being a solution is reaching the k limit
    '''
    Function that verifies if a (partial) solution is a final (complete) solution of the problem
    '''
    return len(solution) == k
def getNext(sol, pos):
    '''
    Function that returns the next element from the definition domain
    '''
    return sol[pos] + 1
def isConsistent(sol,domain,cond):
    isCons = True
    i = 0
    #print("caca",i<len(sol)-1)
    while(i<len(sol)-1) and (isCons==True):
        #print("caca")
        #print(domain[sol[i]],domain[sol[len(sol)-1]])
        if(sol[i] >= sol[len(sol) -1] or not cond(domain[sol[i]],domain[sol[len(sol)-1]])):#check for consistence for the combinations
            isCons = False
        else:
            i = i + 1
    return isCons

def myBracktrackingRec(n,k,solution,domain,cond):#returns the solution list
    '''
    This is a recursive algorithm

    The generation in this case is similar to the combination generation problem
    This function generates combinations of 'k' elements out of 'n' from the 'domain' using a certain condition

    The variable 'cond' is function that provides information about the generation instructions

    The ideea is that i generate the combinations of n taken k (integers), that correspond with the elements from the
    'domain' ,satisfying the 'condition' 

    '''
    initValue = init(domain)
    solution.append(initValue)
    elem = getNext(solution, len(solution) -1)
    while(elem < n):
        solution[len(solution) -1] = elem
        if(isConsistent(solution,domain,cond) == True):
            if(isSolution(solution, k) == True):
                yield solution
            else:
                yield from myBracktrackingRec(n, k, solution[:],domain,cond)
        elem = getNext(solution, len(solution) -1)

def printSolution(sol,domain):
    '''
    Prints one of the 'domain' version of the solution 'sol'
    '''
    for elem in sol:
        print(domain[elem], "\t")
    print("end of group \n")

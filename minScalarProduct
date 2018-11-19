def permutation(a):
    if len(a) == 0:
        return []
    
    if len(a) == 1:
        return [a]
    
    currentpermutation = []
    for i in range(len(a)):
        m = a[i]
        remainingList = a[:i] + a[i+1:]
        
        for p in permutation(remainingList):
            currentpermutation.append([m]+p)
    return currentpermutation


def minScalarProduct(a, b):
    sums = []
    permutations = permutation(b)
    for i in range(len(permutations)):
        sum = 0
        for j in range(len(a)):
            sum = sum + (permutations[i][j]*a[j])
        sums.append(sum)
    print(min(sums))
            
minScalarProduct([1,3,-5],[-2,4,1]) # returns -25

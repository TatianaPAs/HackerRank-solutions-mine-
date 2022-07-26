
def rotLeft(a, d):
    # Write your code here
    #rotate only leftover of the length of array
    d=d%n
    #split array in 2 arrays
    arr1=a[0:d]
    arr2=a[d:n]
    # return joined array
    return arr2+arr1
A = [2,4,6,11,34,56,97,101,355,1245,1400]

def binary_search(low,high,A,x):
    
    while low <=high:
        mid = int((low+high)/2)
        if A[mid] == x:
            print(mid,x)
            return mid
        if A[mid] > x:
            high = mid -1
            return binary_search(low,high,A,x)
        if A[mid] < x:
            low = mid + 1
            return binary_search(low,high,A,x)
    return -1
    
low = 0
high  = len(A) - 1
y = binary_search(low,high,A,101)
print(y)
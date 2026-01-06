def rec_sum(arr,n):
    if n <= 0 :
        return 0
    return rec_sum(arr , n-1) + arr[n-1]


array = [1,2,3,4]

print(rec_sum(array,4))
        
#! For when we want to use another function to find the length of an array

def arraysum(arr):
    return rec_sum(arr , len(arr))

print(arraysum(array))

def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    
    for i in range(1,len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
            
    return smallest_index


def selection_sort(arr):
    
    newarr = []
    
    for i in range(len(arr)):
        
        smallest = findSmallest(arr)
        newarr.append(arr.pop(smallest))
        
    return newarr


lst = [4,2,65,41,5,3]

print(selection_sort(lst))
def binary_search(list1, item):
    
    low = 0
    
    high = len(list1) - 1 
    
    while low <= high :
        
        mid = (high + low) // 2
        
        guess = list1[mid]
        
        if guess == item :
            
            return mid
        
        if guess > item:
            
            high = mid - 1
            
        else:
            
            low = mid + 1
            
    return -1
    
my_list = [1,3,5,7,9]

result = binary_search(my_list,3)

if result != -1:
    print("Found at index :", result)
else:
    print("Not Found")
    
    
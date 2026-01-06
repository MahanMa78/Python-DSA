a = [1,2,3,4,5]
b =0

def count_sum(a , b):
    try :
        if a[b]:        
            b += 1
            count_sum(a , b)
    except:
        print(b)
    
count_sum(a,b)
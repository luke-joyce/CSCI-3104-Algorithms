###Question 3 - h_index
def partition(arr,low,high):
    i = ( low-1 )# index of smaller element 
    pivot = arr[high]# pivot 
    
    for j in range(low , high): 
        if arr[j] <= pivot: 
            
            i = i+1
            arr[i],arr[j] = arr[j],arr[i] 
            
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 ) 
    
    
    
def h_index(arr,low,high): 
    if low < high: 
        
        pi = partition(arr,low,high) 
        
        if arr[pi] <= (len(arr)-pi-1):
            h_index(arr,pi+1,high)
        else:
            h_index(arr,low,pi-1)
    else:
        print("The index is",(len(arr)-low))

    
    
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
n = len(arr) 
h_index(arr,0,n-1)

##Got index 5. Works for all cases.
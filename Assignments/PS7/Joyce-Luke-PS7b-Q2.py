import random
import math
import time

#Question 2
def shuffledArray(n):
    arr=[i for i in range(0,n)]
    for j in range(len(arr)):
        rand = random.randint(0,n-1)
        temp=arr[j]
        arr[j]=arr[rand]
        arr[rand]=temp
    return arr

def flipSelectionSort(arr):
    flips=0
    for i in range(len(arr)): 
        min_idx = i 
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]: 
                min_idx = j
        
        flips+=min_idx - i
        arr.insert(i, arr[min_idx])
        del arr[min_idx+1]
    return flips


def flipsAndSort(arr, p, r):
    t = 0
    if (p<r):
        q=int((p+r)/2)
        t = flipsAndSort(arr,p,q)
        t = t + flipsAndSort(arr,q+1,r)
        t = t + mergeSort(arr,p,q,r)
    return t

def mergeSort(arr,p,q,r):
    flips = 0
    i = 0
    j = 0
    k = p
    low = []
    high = []
    for s in range(p,q+1):
        low.append(arr[s])
    for t in range(q+1,r+1):
        high.append(arr[t])
    while (i<(q-p+1) and j<(r-q)):
        if (low[i]<=high[j]):
            arr[k]=low[i]
            i=i+1
        else:
            arr[k]=high[j]
            flips=flips+(q-p-i+1)
            j=j+1
        k=k+1
    while(i<(q-p+1)):
        arr[k]=low[i]
        i=i+1
        k=k+1
    while(j<(r-q)):
        arr[k]=high[j]
        j=j+1
        k=k+1
    return flips

print("----------Question 2.a.iv-----------")
for i in range(1,13):
    length=int(math.pow(2,i))
    arr = shuffledArray(length)
    arr_2 = arr[:]
    print(flipsAndSort(arr, 0, length-1),"\t\t",flipSelectionSort(arr_2))
          
   
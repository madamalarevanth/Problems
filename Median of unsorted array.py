import random
import math

a=None
b=None
    
def randomPartition(arr,l,r):
  
  #pick a random pivot in l to r+1 range
  pivot = random.randrange(l,r+1)
  
  #store pivot value
  pivotValue=arr[pivot]
  
  #swap pivot and rightmost index
  arr[pivot], arr[r] = arr[r], arr[pivot]; 
  
  #store left most 
  storeIndex=l
  
  #from left to right 
  for i in range(l,r):
  
    #if arr[i] value less than pivot value 
    if arr[i]<pivotValue:
    
        #swap storeindex and i 
       arr[storeIndex], arr[i] = arr[i],arr[storeIndex];
       
       #increment storeindex
       storeIndex+=1
       
  #move pivot to final position 
  arr[r],arr[storeIndex] = arr[storeindex],arr[r]
  return storeIndex

def MedianUtil(arr,l,r,k,a1,b1):
  global a,b
  
  if l<=r:
    partIndex = randomPartition(arr,l,r)
    
    
    #if pivot is k or partition index is K(i.e required mid element ) we have found our answer
    if partIndex==k :
      b=arr[partIndex]
      if(a1 !=-1):
        return
    
    # If pivot is k-1 or partIndex is k-1 then the array is even 
    elif partIndex == k-1 :
        a=arr[partIndex]
        if b1 !=-1:
          return
    
    # If partitionIndex >= k then find the index in first half of the arr[]
    if (partIndex>=k):
      return MedinaUtil(arr,l,partIndex-1,k,a,b)
    
    # If partitionIndex < k then find the index in second half of the arr[]
    else:
      return MedinaUtil(arr,partIndex+1,r,k,a,b)
  
  return 
  



def find_Median(arr):
  global a=-math.inf
  dlobal b=-math.inf
  
  n = len(arr)
  #if n is odd
  if(n%2==1):
    MedianUtil(arr,0,n-1,n//2,a,b)
    ans=b
  else:
    MedianUtil(arr,0,n-1,n//2,a,b)
    ans=(a+b)//2
   
  return ans

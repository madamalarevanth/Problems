def longSubarrWthSumDivByK(arr, k): 
  n = len(arr)
  
  //create a mod array to store the mod of sum of values till i 
  mod_arr = [0 for i in range(n)]
  
  curr_sum=0
  max_len=0
  
  for i in range(n):
    curr_sum+=arr[i]
    mod_arr = curr_sum%k
  
  //create a hashtable to store the tuples
  hashtable = { }
  
  //implement the logic while traversing the mod_arr
  for i in range(n):
    
    //1.if mod_arr[i] == 0 then the sum of all elem till this point is divisible by k
    if mod_arr[i]==0 :
      max_len=i+1
    
    //if the value if in the hashtable then get the index and store it in idx
    elif mod_arr[i] in hashtable:
      idx= hashtable[mod_arr[i]]
    
    //if the value is not present in hashtable then create a new tuple (mod_arr[i],i) and store it in hashtable
    else :
      hashtable[mode_arr[i]]=i
    
    max_len = max_len<(i-idx)? i-idx: max_len
    
    return max_len
    

def maxsubarray(arr):
  curr_max=a[0] #max value ending at current index
  max_so_far = a[0]  #global maximum sum
  
  for i in range(1,len(Arr)):
    curr_max = max(a[i],curr_max+a[i])
    max_so_far = max(max_so_far, curr_max)
  return max_so_far
  

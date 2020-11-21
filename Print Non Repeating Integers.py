def uniqueNumbers(arr):
  sum =0
  # calculate the xor of all the values in the given array 
  # xor of two same value is zero i.e, it removes the duplicate values when there are two duplicates
  #calculating the xor of all the values in arr gives bit wise sum of the two unique no's
  for i in range(len(arr));
    sum = sum^arr[i]
  #create the mask which contains the right most unique bit in the two numbers which can be obtained by 2's complement of the sum 
    mask = sum &~(sum)
  
  #using this mask perform and & operator divide the arr into two parts oen part contains one unique no and other part has other
  #this is possible by &ing the mask with each number as there are only two options i.e a number has bit value similar to mask or not so we get two groups 
  sum1=0
  sum2=0
  for i in  range(len(arr)):
    if(mask&arr[i] == 0):
      sum1 ^= arr[i]
    else:
      sum2 ^= arr[i]
  #as we are xoring while collecting values into the duplicates diminshes leaving only unique values
  print(sum1,sum2)
  

def findTriplets(a,n):
    
    # sorint the array elements
    a.sort()
    
    # traversing the elements to find the triplets
    for i in range(n-2):
        l=i+1
        r=n-1
        
        # find the two elements which can sum upto 0
        # with the element at ith index
        while(l<r):
            curr_sum=a[i]+a[l]+a[r]
            
            # if they sum upto 0 then true
            if(curr_sum==0):
                return 1
            # else if the sum is less than 0
            elif(curr_sum<0):
                l+=1
            # else if sum is greater than 0
            else:
                r-=1
    return 0

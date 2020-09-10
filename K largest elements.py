#code
from heapq import heappop, heappush, heapify 

t = int(input())

for _ in range(t):
    n, k = map(int,input().strip().split())
    arr = list(map(int,input().strip().split()))[:n]
    
    heap=[]
    heapify(heap)
    for val in arr:
        heappush(heap, val)
        if (len(heap)>k):
            heappop(heap)
    res=[]
    for i in range(k):
        res.append(heappop(heap))
    
    for i in range(len(res)):
        print(res[len(res)-1-i],end=' ')
    print( )
        

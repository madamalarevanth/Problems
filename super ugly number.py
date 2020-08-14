import heapq

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        #cand contains possible candidates for ugly numbers
        cand = [(p,p,1) for p in primes]
        
        #as it is not garunteed that primes are in ascending order
        heapq.heapify(cand)
        
        #ugly_num is the list of ugly numbers generated
        ugly_nums = [1]
        
        #required nth ugly number so do n times 
        for _ in range(n-1):
            #add least possible ugly number formed by primes
            ugly_nums.append(cand[0][0])
            
            while(cand[0][0] == ugly_nums[-1]):
                #popping the smallest candidate
                x,p,i = heapq.heappop(cand)
                
                #push the next possible least ugly number
                #(i.e smallest cand * present ugly number) into cand 
                heapq.heappush(cand,(p*ugly_nums[i],p,i+1))
                
        return ugly_nums[-1]
                

class Solution:
    def kth_smallest_element(self, A, k):
        lenA = len(A)
        
        if k > lenA:
            return -1
        
        lower = min(A)
        high = max(A)
        
        while lower <= high:
            mid = int(lower + (high - lower) / 2)       
            equals = 0
            less = 0
            
            for item in A:
                if item < mid:
                    less += 1
                elif item == mid:
                    equals += 1            
                if less >= k:
                    break
            
            if less < k and less + equals >= k:
                return mid
            elif less >= k:
                high = mid - 1
            else:
                lower = mid + 1
                    
        return -1
       
        
    def num_range(self, A, b, c):
        lenA = len(A)
        start = 0
        i = 0
        sumA = 0
        
        count = 0
        
        while start < lenA :
            sumA += A[i]
            if (b <= sumA and sumA <= c):
                count += 1
            elif sumA >= c:
                i = start + 1
                sumA = 0
            i += 1
            
            if i == lenA:
                sumA = 0
                start += 1
                i = start
                
        return count
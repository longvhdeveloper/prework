class Solution:    
    def longest_consecutive_sequence(self, A):
        s = set()    
        ans = 0
        for item in A:
            s.add(item)
            
        for i in range(len(A)):        
            if (A[i] - 1) not in s:
                j = A[i]
                while j in s:
                    j += 1            
                ans = max(ans, j - A[i])
                
        return ans
            

    def permutation(self, A):
        if len(A) == 0:
            return []
        
        if len(A) == 1:
            return [A]
            
        permutation_list = []
        
        for i in range(len(A)):
            m = A[i]        
            l = A[:i] + A[i+1:]
            #print(l)
            #print("===========")
            for per in permutation(l):
                permutation_list.append([m] + per)
        return permutation_list
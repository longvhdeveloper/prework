class Solution:
    def next_greater(self, A):
    ans = []
    for i in range(len(A)):
        greater = -1
        for j in range(i+1, len(A)):
            if A[i] < A[j]:
                greater = A[j]
                break
        ans.append(greater)
        
    return ans
class Solution:
    def print_matrix(self, n):
        ans = []
        row_len = 2 * n - 1
        col_len = 2 * n - 1 
        
        template = [0 for _ in range(col_len)]
        number = n
        start = 0
        end = col_len
        
        direc = 1
        
        for row in range(row_len):        
            for col in range(start, end):
                template[col] = number         
            ans.append(" ".join([str(item) for item in template]))
            start += direc
            end -= direc
            number -= direc
            
            if start > end:
                direc = -1
                start -= 1
                end += 1
                number += 2
        return "\n".join(ans)
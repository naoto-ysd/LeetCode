class Solution(object):
    def arrangeCoins(self, n):      
        lower_bound, upper_bound = 1, n
        
        while lower_bound <= upper_bound:
            k = lower_bound + (upper_bound-lower_bound)//2
            k_total = (k*(k+1))//2 # this part is a key point of solving this question.
            if k_total == n:
                return k
            elif k_total > n:
                upper_bound = k-1
            else:
                lower_bound = k+1
        
        return upper_bound

obj = Solution()
ret = obj.arrangeCoins(8)
print(ret)
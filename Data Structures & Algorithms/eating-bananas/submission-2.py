class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        r=max(piles)
        res=r
        while l <= r:
            k=(l+r)//2
            times=0
            for p in piles:
                times+=math.ceil(p/k)
            if times <=  h:
                res=min(res,k)
                r=k-1
            else:
                l=k+1
        return res
            

            


        
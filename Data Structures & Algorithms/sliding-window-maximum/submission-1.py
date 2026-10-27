class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output=[]
        q = collections.deque() #index
        l= 0
        r=0
        while r < len(nums):
            while q and nums[q[-1]] < nums[r]: #가장 작은 값보다 현재값이 더 크면
                q.pop() #가장 작은 값을 뺀다
            q.append(r)

            if l > q[0]:
                q.popleft() #윈도우에서 빠져야 하는 값
            if(r+1) >= k:
                output.append(nums[q[0]])
                l+=1
            r+=1
        return output

        
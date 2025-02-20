# Problem link - https://leetcode.com/problems/find-unique-binary-string/


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n=len(nums)
        arr=set()
        for i in range(n):
            arr.add(int(nums[i],2))
        ans=0
        for i in range(2**n):
            if i not in arr:
                ans=i
                break
        bl='0'+str(n)+'b'
        return format(ans,bl)

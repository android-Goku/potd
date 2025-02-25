# Problem Link - https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/

class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        m = 10**9 + 7
        o, e = 0, 1
        pfx = 0
        ans = 0

        for i in arr:
            pfx += i
            if pfx % 2 == 0:
                ans = (ans + o) % m
                e += 1
            else:
                ans = (ans + e) % m
                o += 1

        return ans
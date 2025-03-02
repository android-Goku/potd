# Problem link - https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values/description/

class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        n=len(nums1)
        m=len(nums2)
        d = dict()
        for i in range(n):
            if(str(nums1[i][0]) in d):
                d[str(nums1[i][0])] +=  nums1[i][1]
            else:
                d[str(nums1[i][0])] =  nums1[i][1]
        
        for i in range(m):
            if(str(nums2[i][0]) in d):
                d[str(nums2[i][0])] +=  nums2[i][1]
            else:
                d[str(nums2[i][0])] =  nums2[i][1]

        ans =[]

        for i in d:
            ans.append((int(i),d[i]))
        ans.sort()

        return (ans)
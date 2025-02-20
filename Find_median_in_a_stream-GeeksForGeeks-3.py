# Problem link - https://www.geeksforgeeks.org/problems/find-median-in-a-stream-1587115620/1


class Solution:
    def getMedian(self, arr):
        import bisect
        sl=[]
        n=len(arr)
        mid=[]
        for i in range(n):
            bisect.insort(sl,arr[i])
            if(i%2==0):
                mid.append(sl[i//2])
            else:
                mid.append(( sl[i//2] + sl[(i//2)+1] ) / 2 )
        return mid

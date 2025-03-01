#Problem link - https://leetcode.com/problems/apply-operations-to-an-array/

for t in range(int(input())):
    nums = list(map(int,input().split()))
    n = len(nums)
    arr=[]
    for i in range(n-1):
        if(nums[i]==nums[i+1]):
            nums[i] = nums[i]*2
            nums[i+1]=0
    
    for i in range(n):
        if (nums[i]>0):
            arr.append(nums[i])
    
    zeros = n - len(arr)
    print( arr+[0]*zeros)
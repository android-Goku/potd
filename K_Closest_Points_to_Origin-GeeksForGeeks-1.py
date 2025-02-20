# Prolem link - https://www.geeksforgeeks.org/problems/k-closest-points-to-origin--172242/1

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Your code here
        distArray=[]
        for i in range(len(points)):
            eDist = ((points[i][0]**2) + (points[i][1]**2))**0.5
            distArray.append((eDist,i))
        distArray.sort()
        
        for i in range(k):
            distArray[i]=points[distArray[i][1]]
        return distArray[:k]


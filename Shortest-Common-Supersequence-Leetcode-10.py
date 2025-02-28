# Problem Link - https://leetcode.com/problems/shortest-common-supersequence/

class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m, n = len(str1), len(str2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Fill the dp table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        # Backtrack to find the LCS string
        lcs = []
        i, j = m, n
        while i > 0 and j > 0:
            if str1[i - 1] == str2[j - 1]:
                lcs.append(str1[i - 1])
                i -= 1
                j -= 1
            elif dp[i - 1][j] > dp[i][j - 1]:
                i -= 1
            else:
                j -= 1

        common =  "".join(reversed(lcs))
        s,s1,s2 = 0,0,0
        ans = ""
        while s < len(common):
            #print(s,s1,s2, ans)
            if(common[s] == str1[s1] and common[s] == str2[s2]):
                ans+=common[s]
                s+=1
                s1+=1
                s2+=1

            elif(common[s] != str1[s1]):
                ans+=str1[s1]
                s1+=1
            elif(common[s] != str2[s2]):
                ans+=str2[s2]
                s2+=1
        
        if(s1<=len(str1)-1):
            ans+=str1[s1:]
        if(s2<=len(str2)-1):
            ans+=str2[s2:]
        return ans
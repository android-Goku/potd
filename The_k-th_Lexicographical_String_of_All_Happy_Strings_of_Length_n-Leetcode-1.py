# Problem link - https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/description/


class Solution:
    def getHappyString(self, n: int, k: int) -> str:
            maxHappy = 3 * (2**(n-1))
            ans=""
            if(k <= maxHappy):
                ans = ""
                first = True
                while( n > 0):
                    q = k // (2**(n-1))
                    r = k % (2**(n-1))
                    if (first):
                        d=q+int(r>0)
                        if(d==1):
                            ans+="a"
                        elif(d==2):
                            ans+="b"
                        else:
                            ans+="c"
                        first=False
                    else:
                        d=q+int(r>0)
                        if(d>1):
                            if(ans[-1]=="a"):
                                ans+="c"
                            elif(ans[-1]=="b"):
                                ans+="c"
                            else:
                                ans+="b"
                        else:
                            if(ans[-1]=="a"):
                                ans+="b"
                            elif(ans[-1]=="b"):
                                ans+="a"
                            else:
                                ans+="a"
                    if(r > 0):
                        k=r
                    n-=1
            return ans


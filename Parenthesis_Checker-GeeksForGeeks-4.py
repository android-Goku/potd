# Problem link - https://www.geeksforgeeks.org/problems/parenthesis-checker2744/1


class Solution:
    def isBalanced(self, s):
        # code here
        checker = []
        length =len(s)
        for i in range(length):
            if( len(checker) == 0 ):
                checker.append(s[i])
            else:
                top = checker[-1]
                if( top == '(' and s[i] == ")"):
                    checker.pop()
                elif( top == '{' and s[i] == "}"):
                    checker.pop()
                elif( top == '[' and s[i] == "]"):
                    checker.pop()
                else:
                    checker.append(s[i])
        return (len(checker) == 0) 

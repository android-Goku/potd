#Problem link - https://www.geeksforgeeks.org/problems/longest-valid-parentheses5657/1

for i in range(int(input())):
    s = input()
    stack=[-1]
    maxy = 0
    for i in range(len(s)):
        print(i,stack)
        if(s[i] == '('):
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i)
            else:
                maxy = max(maxy, i-stack[-1])
    print(maxy)
    print(stack)


#()()
# ))
# ()
@)))))(())())))()))))()((()(((((((()(()()))()(()())))                  



# ()()
# ))
# ()
# )))))
# (())()
# )))
# ()
# ))))
# ()
# ((
#     ()
#     ((((
#         (((()(()()))()(()())))
#         ((
#             ()
#             ((((((()))))()(())(((((())((((((((()))((())()(()())()(()(()(()))))))))))))))()
              
#()()))())))))(())())))()))))()((()(((((((()(()()))()(()())))((()((((((()))))()(())(((((())((((((((()))((())()(()())()(()(()(()))))))))))))))()

# Problem link - https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        pId=[0]
        def recover(preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
            if len(preorder) < 1 or len(postorder) < 1 or pId[0] > len(preorder):
                return None
            
            root = TreeNode(preorder[pId[0]])
            
            #print("--> root", root, preorder, postorder, pId)
            
            if(len(postorder)==1):
                #print("=====================")
                pId[0]+=1
                return root

            else:
                pId[0]+=1
                lc=preorder[pId[0]]
                li=0
                for i in range(len(postorder)):
                    if(postorder[i]==lc):
                        li=i
                        break
                #print("===> lc,li, pId",lc, li,pId)
                postorder=postorder[:-1]
                root.left = recover(preorder,postorder[:li+1])
                root.right = recover(preorder,postorder[li+1:])
                return root
        return recover(preorder,postorder)

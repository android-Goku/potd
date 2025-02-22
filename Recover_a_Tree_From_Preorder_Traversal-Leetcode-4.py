# Problem link - https://leetcode.com/problems/recover-a-tree-from-preorder-traversal

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrder(self,preorder):
    length=len(preorder)
    cdash = 0
    pdash = 0
    currenNumber=''
    level=[]

    for i in range(length):
        #print("Index",i,preorder[i],"level",level, "cdash",cdash)
        if( preorder[i] != '-' ):
            currenNumber+=preorder[i]
            if ( i != 0 and preorder[i-1]=='-'):
                pdash=cdash
                cdash=0
        else:
            cdash+=1
            #print("------> Current Number ", currenNumber, "pdash", pdash, "cdash", cdash, level)
            if(len(currenNumber)>0):
                if(len(level) <= pdash):
                    level.append([[currenNumber,i]])
                else:
                    level[pdash].append([currenNumber,i])
            currenNumber = ''
    if(len(currenNumber)>0):
        if(len(level) <= pdash):
            level.append([[currenNumber,i]])
        else:
            level[pdash].append([currenNumber,i])
    #print("------> Current Number ", currenNumber, "pdash", pdash, "cdash", cdash, level)
    #print(level)
    return level

def recoverTree(self,levelOrder):
    root=TreeNode(int(levelOrder[0][0][0]))
    levelOrder[0][0].append(root)

    for i in range(1,len(levelOrder)):
        parent = 0
        #print ("----> Parent, left, right", parent)
        for child in levelOrder[i]:
            cIdx = child[1]
            childNode = TreeNode(int(child[0]))
            child.append(childNode)
            #print("....> cIdx childe", cIdx, child)

            while parent < len(levelOrder[i-1]):
                if (levelOrder[i-1][parent][1] < cIdx):
                    parent+=1
                else:
                    break
                #print("parent ---->", parent)
            parent-=1
            if(parent <0):
                parent =0
            #print ("Parent ", parent, cIdx, levelOrder[i-1][parent][1])
            #print("=====> parent , level[i-1]", parent, levelOrder[i-1])
            if(levelOrder[i-1][parent][2].left == None):
                levelOrder[i-1][parent][2].left = childNode

            elif( levelOrder[i-1][parent][2].left != None and levelOrder[i-1][parent][2].right == None ):
                levelOrder[i-1][parent][2].right = childNode
    #print(levelOrder)
    return root

for i in range(int(input())):
    preorder = input()
    levels=levelOrder(preorder)
    root = recoverTree(levels)




# [
#     [('1', 1)],
#     [('2', 3), ('5', 12)],
#     [('3', 6), ('6', 15)],
#     [('4', 10), ('7', 18)]
# ]

# [
#     [('1', 1)],
#     [('401', 5)], 
#     [('349', 10), ('88', 18)], 
#     [('90', 15)]
# ]

# [
#     [('1', 1)], 
#     [('2', 3), ('5', 11)], 
#     [('3', 6), ('4', 9), ('6', 14), ('7', 16)]
# ]
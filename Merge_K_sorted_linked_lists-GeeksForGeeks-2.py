#Problem link - https://www.geeksforgeeks.org/problems/merge-k-sorted-linked-lists/1


#User function Template for python3
'''
class Node:
    def _init_(self,x):
        self.data = x
        self.next = None
'''
class Solution:
    def mergeKLists(self, arr):
        # code here
        # return head of merged list
        #print(arr, arr[0].data)
        length=len(arr)
        if(length==1):
            return arr[0]
        elif(len(arr)==2):
            head_1 = arr[0]
            head_2 = arr[1]
            head = head_1
            
            while( head_1 != None and head_2 != None ):
                #print(head_1.data)
                if (head_1.data > head_2.data):
                    head_b=head_2
                    head_2=head_2.next
                    head_b.next=head_1.next
                    head_1.next=head_b
                    head_1.data,head_b.data=head_b.data,head_1.data
                    
                else:
                    if(head_1.next != None):
                        head_1=head_1.next
                    else:
                        break
            if(head_2 != None):
                head_1.next = head_2
            return head
        else:
            mid=length//2
            l1=self.mergeKLists(arr[:mid])
            l2=self.mergeKLists(arr[mid:])
            return self.mergeKLists([l1,l2])

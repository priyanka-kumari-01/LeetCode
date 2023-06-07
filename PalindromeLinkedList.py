#Palindrome Linked List: https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode) -> bool:

        # List to store the values of the linked list
        values = []
        # Set the current node to the head of the linked list
        curr = l1
        while curr:
            # Convert the integer value to a string and add it to the list
            values.append(str(curr.val))  
            # Move to the next node
            curr = curr.next

        # Check if the list is a palindrome (same forwards and backwards)    
        return (values == values[::-1])

# Create linked lists
list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(2)
list1.next.next.next = ListNode(1)

# Create Solution instance
print(Solution.mergeTwoLists(1,list1))
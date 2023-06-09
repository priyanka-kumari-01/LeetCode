#Middle of the Linked List: https://leetcode.com/problems/middle-of-the-linked-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

# Create linked lists
list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(5)
list1.next.next.next = ListNode(4)
list1.next.next.next.next = ListNode(1)

# Create an instance of the Solution class
solution = Solution()

# Find the middle node
middle = solution.middleNode(list1)

# Print the values of the middle node and the nodes after it
print("middle")
while middle:
    print(middle.val)
    middle = middle.next
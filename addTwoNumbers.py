#Add Two Numbers: https://leetcode.com/problems/add-two-numbers/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def addTwoNumbers(l1, l2):
        # Create a dummy node to serve as the head of the merged list
        dummy = ListNode(0)
        current = dummy
        carry = 0

        # Iterate until both lists and the carry are empty
        while l1 or l2 or carry:
            sum_val = carry

            # If list1 has remaining nodes, add the value of the current node to the sum and move to the next node.
            if l1:
                sum_val += l1.val
                l1 = l1.next
            # If list2 has remaining nodes, add the value of the current node to the sum and move to the next node.    
            if l2:
                sum_val += l2.val
                l2 = l2.next

            # Calculate the carry for the next iteration
            carry = sum_val // 10
            # Create a new node with the remainder of the sum (0-9)
            current.next = ListNode(sum_val % 10)
            current = current.next

        return dummy.next

# Create linked lists
list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)

list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)

merged_list = ListNode.addTwoNumbers(list1, list2)
# Print the merged list
while merged_list:
    print(merged_list.val)
    merged_list = merged_list.next

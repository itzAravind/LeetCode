class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur = dummy = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1, cur = list1.next, list1
            else:
                cur.next = list2
                list2, cur = list2.next, list2

        if list1 or list2:
            cur.next = list1 if list1 else list2

        return dummy.next
    
 """This code defines a class Solution that has a method mergeTwoLists. This method takes two linked lists, list1 and list2, as input, and merges them into a new sorted linked list.

The method creates two variables cur and dummy, both initialized to a new instance of the ListNode class, which represents a node in the linked list. cur is used to keep track of the current node, and dummy is used to keep track of the head node of the new linked list.

The method then enters a loop that continues as long as both list1 and list2 are not None. Within this loop, the method compares the values of the first nodes of list1 and list2. If the value of list1 is less than the value of list2, the current node cur is set to list1 and list1 is moved to the next node. If the value of list2 is less than or equal to the value of list1, the current node cur is set to list2, and list2 is moved to the next node.

After the loop exits, the method checks if either list1 or list2 still has any nodes remaining. If either list is not empty, the method appends the remaining nodes to the end of the new linked list.

Finally, the method returns the next node of dummy, which represents the head of the new linked list."""

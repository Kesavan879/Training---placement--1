
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow=head
        fast=head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow==fast:
                return True
        return False

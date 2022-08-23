class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = slow = head 
        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next
        return slow
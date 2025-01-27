# Solotion type 1 - List storing technique
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes = []
        while head:
            nodes.append(head)
            head = head.next
        middle = len(nodes) // 2
        
        return nodes[middle]

# Solotion type 2 - Two-Pointer Technique
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow_move = head 
        fast_move = head 
        while fast_move is not None and fast_move.next is not None:
            slow_move = slow_move.next
            fast_move = fast_move.next.next
        
        return slow_move
# Time Complexity : O(m + n), where m and n are the lengths of the two linked lists
# Space Complexity : O(1), no extra space used
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

# Your code here along with comments explaining your approach
# I used the two-pointer technique to equalize traversal distance.
# If one pointer reaches the end of a list, I redirect it to the head of the other list.
# If the two lists intersect, the pointers will meet at the intersection node after at most m + n steps.
# If they don't intersect, both pointers will become None simultaneously.
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None

        ptrA, ptrB = headA, headB

        while ptrA != ptrB:
            ptrA = ptrA.next if ptrA else headB
            ptrB = ptrB.next if ptrB else headA

        return ptrA  # Could be the intersection node or None if no intersection

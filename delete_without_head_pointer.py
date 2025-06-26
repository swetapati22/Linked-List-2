# Time Complexity : O(1)
# Space Complexity : O(1)
# Did this code successfully run on Leetcode : No (GFG)
# Any problem you faced while coding this : No

# Your code here along with comments explaining your approach
# Since we are not given the head of the list, and the node to be deleted is not the last one,
# I copied the data from the next node into the current node, and then bypassed the next node.
# This effectively deletes the current node by overwriting it and unlinking its successor.
class Solution:
    def deleteNode(self, del_node):
        if del_node is None or del_node.next is None:
            return  # Cannot delete if it's the last node

        del_node.data = del_node.next.data
        del_node.next = del_node.next.next

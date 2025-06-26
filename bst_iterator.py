# Time Complexity : 
# - next() and hasNext() run in average O(1) time over n calls, where n is the number of nodes

# Space Complexity : O(h), where h is the height of the tree used by the stack

# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

# Your code here along with comments explaining your approach
# I used an explicit stack to simulate in-order traversal iteratively.
# During initialization, I pushed all left children of the root into the stack.
# next() pops the top node (smallest unvisited), and then pushes its right child's left path.
# hasNext() simply checks if the stack is non-empty.

class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self._leftmost_inorder(root)

    def _leftmost_inorder(self, node):
        # Push all the leftmost nodes to the stack
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        # Pop the smallest element
        top_node = self.stack.pop()
        # If there's a right child, process its leftmost path
        if top_node.right:
            self._leftmost_inorder(top_node.right)
        return top_node.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
        self.next = None

    def __eq__(self, other):

        if self.val == other.val:

            if self.left and other.left:
                return self.left == other.left

            if self.right and other.right:
                return self.right == other.right

            if not (self.left and other.left) and not (self.right and other.right):
                return True

        return False

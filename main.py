class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    # preorder traversal: traverse left nodes first

    def serialize(self, root):
        res = []
        self.serialize_recursive(root, res)
        return ",".join(res)

    def serialize_recursive(self, root, res):
        if root is None:
            res.append("N")
        else:
            res.append(str(root.val))
            self.serialize_recursive(root.left, res)
            self.serialize_recursive(root.right, res)

    def deserialize(self, data):
        vals = data.split(",")
        self.index = 0

        return self.deserialize_rescursive(data)

    def deserialize_rescursive(self, data):
        if data[self.index] == "N":
            self.index += 1
            return None
        node = TreeNode(int(data[self.index]))
        self.index += 1
        node.left = self.deserialize_rescursive(data)
        node.right = self.deserialize_rescursive(data)

        return node


codec = Codec()

node = TreeNode(1)
node.left = TreeNode(2)
node.left.left = TreeNode(10)
node.right = TreeNode(3)
node.right.right = TreeNode(4)
node.right.left = TreeNode(5)

codec.serialize(node)

data = "1,2,10,N,N,N,3,5,N,N,4,N,N"

breakpoint()

codec.deserialize(data)

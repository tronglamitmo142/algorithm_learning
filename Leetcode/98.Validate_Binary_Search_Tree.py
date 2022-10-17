class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        list_node = []
        def inorder(node):
            if node != None:
                inorder(node.left)
                print(node.val)
                list_node.append(node.val)
                inorder(node.right)
        inorder(root)
        print(list_node)
        for i in range(1, len(list_node)):
            if list_node[i-1] >= list_node[i]:
                return False
        return True
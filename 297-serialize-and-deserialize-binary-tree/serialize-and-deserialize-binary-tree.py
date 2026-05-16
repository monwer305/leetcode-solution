# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        ser = ""
        if not root:
            return ser
        queue = deque()
        queue.append(root)
        ser=str(root.val)
        while queue:
            cur = queue.popleft()

            if cur.left:
                ser= f"{ser},{str(cur.left.val)}"
                queue.append(cur.left)
            else:
                ser= f"{ser},n"

            if cur.right:
                ser= f"{ser},{str(cur.right.val)}"
                queue.append(cur.right)
            else:
                ser= f"{ser},n"
        
        return ser
            

            

        

        
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

        root = None

        if data == "":
            return None

        str_list =  data.split(",")


        root = TreeNode(int(str_list[0]))

        queue = deque()
        queue.append(root)

        ind = 0

        while(queue):
            cur = queue.popleft()

            left = None
            right = None
            ind+=1
            if str_list[ind] != "n":
                left = TreeNode(int(str_list[ind]))
                queue.append(left)

            ind+=1
            
            if str_list[ind] != "n":
                right = TreeNode(int(str_list[ind]))
                queue.append(right)
            
            cur.left = left
            cur.right = right
        
        return root
            



        
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
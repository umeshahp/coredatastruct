

templist = []
class Node:
    def __init__(self, value):
        self.data = value
        self.right = None
        self.left = None


class BST:
    def __init__(self):
        self.root = None

    def create_newnode(self, value):
        node = Node(value)
        return node

    def find2insert(self,root, node):
        ''''''
        if root is  None:
            self.root = node
        elif root.data < node.data:
            if root.right is None:
                root.right = node
            else:
                self.find2insert(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                self.find2insert(root.left, node)

    def insert(self,  value):
        # if 'new_node'  in locals() or 'new_node'  in globals():
        #     pass
        # else:
        new_node = self.create_newnode(value)
        if self.root is None:
            self.root = self.create_newnode(value)
            return self.root
        else:
            self.find2insert(self.root, new_node)



    def traverse_postorder(self,root):
        global templist
        if root:
            self.traverse_preorder(root.left)
            self.traverse_preorder(root.right)
            print(root.data)


    def traverse_inorder(self,root):
        if root:
            self.traverse_inorder(root.left)
            print(root.data)

            self.traverse_inorder(root.right)

    def traverse_preorder(self,root):
        if root:
            print(root.data)
            self.traverse_preorder(root.left)
            self.traverse_preorder(root.right)

    def min_value(self, root):
        current = root
        while current.left:
            current = current.left
        return current

    def delete(self, root, key):

        if not root:
            return root

        if root.data > key:
            root.left = self.delete(root.left, key)

        elif root.data < key:
            root.right = self.delete(root.right, key)

        else:
            if not root.right:
                return root.left
            if not root.left:
                return root.right
            temp_val = root.right
            mini_val = temp_val.data
            while temp_val.left:
                temp_val = temp_val.left
                mini_val = temp_val.data

            root.val = mini_val
            # Delete the minimum node in right subtree
            root.right = self.delete(root.right, root.data)
        return root


    def search_by_key(self, root ,value):
        if root is None:
            return False
        elif root.data == value :
            return True
        elif root.data < value :
            return self.search_by_key(root.right, value)
        else:
            return self.search_by_key(root.left, value)



if __name__ == '__main__':
    bst = BST()
    bst.insert(10)
    #bst.traverse_inorder(bst.root)
    lis = [1, 2, 3 ,44, 0,11,  33 , 45, 55]
    for it in lis:
        bst.insert(it)
    #bst.traverse_inorder(bst.root)
    print('\n')
    bst.traverse_postorder(bst.root)
    print("\n")
    #bst.traverse_preorder(bst.root)
    print(bst.search_by_key(bst.root, 2111))
    bst.delete(bst.root, 1)
    bst.traverse_postorder(bst.root)

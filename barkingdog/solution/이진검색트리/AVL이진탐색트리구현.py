import sys

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key
        self.height = 1

class AVLTree:
    def insert(self, node, key):
        # 1. Perform the normal BST insert
        if node is None:
            return Node(key)
        elif key < node.value:
            node.left = self.insert(node.left, key)
        else:
            node.right = self.insert(node.right, key)

        # 2. Update height of this ancestor node
        return self.rebalance(node)

    def delete(self, node, key):
        # Step 1 - Perform standard BST delete
        if not node:
            return node

        if key < node.value:
            node.left = self.delete(node.left, key)
        elif key > node.value:
            node.right = self.delete(node.right, key)
        else:
            # This is the node to be deleted
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                # Node with two children, get the inorder successor (smallest in the right subtree)
                temp = self.getMinValueNode(node.right)
                node.value = temp.value
                # Delete the inorder successor
                node.right = self.delete(node.right, temp.value)

        # If the tree had only one node then return
        if node is None:
            return node

        # 2. Update height of this ancestor node
        return self.rebalance(node)

    def rebalance(self, node):
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        balance = self.get_balance(node)

        # Left Left
        if balance > 1 and self.get_balance(node.left) >= 0:
            return self.rotate_right(node)

        # Left Right
        if balance > 1 and self.get_balance(node.left) < 0:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)

        # Right Right
        if balance < -1 and self.get_balance(node.right) <= 0:
            return self.rotate_left(node)

        # Right Left
        if balance < -1 and self.get_balance(node.right) > 0:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node

    def getMinValueNode(self, node):
        if node is None or node.left is None:
            return node
        return self.getMinValueNode(node.left)
    
    def getMaxValueNode(self, node):
        if node is None or node.right is None:
            return node
        return self.getMaxValueNode(node.right)
    
    def delete_min(self, node):
        if node is None:
            return node
        elif node.left is None:
            return node.right
        else:
            node.left = self.delete_min(node.left)
            return self.rebalance(node)
        
    def delete_max(self, node):
        if node is None:
            return node
        elif node.right is None:
            return node.left
        else:
            node.right = self.delete_max(node.right)
            return self.rebalance(node)

    def rotate_left(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def rotate_right(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        return x

    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def pre_order(self, root):
        res = []
        if root:
            res.append(root.value)
            res = res + self.pre_order(root.left)
            res = res + self.pre_order(root.right)
        return res


for _ in range(int(input().rstrip())):
    tree = AVLTree()        # 새로 초기화할 필요는 없다. 
    root = None
    for _ in range(int(input().rstrip())):
        querry, num = sys.stdin.readline().split()
        if querry == 'I':
            root = tree.insert(root, int(num))
        elif not root:
            continue
        else:
            if num == '-1':
                root = tree.delete_min(root)
            else:
                root = tree.delete_max(root)

    if not root:
        print('EMPTY')
    else:
        print(tree.getMaxValueNode(root).value, tree.getMinValueNode(root).value)

import random

class AVLNode:

    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None
        self.height = 1

    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.item
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.item
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.item
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.item
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2
    
class AVLTree:

    def insert(self, root, val):

        if not root:
            return AVLNode(val)
        elif val < root.item:
            root.left = self.insert(root.left, val)
        else:
            root.right = self.insert(root.right, val)

        root.height = 1 + max(self.get_height(root.right), self.get_height(root.left))

        balance = self.get_balance(root)

        if balance < -1 and val < root.left.item:
            return self.rotateRight(root)
        elif balance < -1 and val > root.left.item:
            root.left = self.rotateLeft(root.left)
            return self.rotateRight(root)
        elif balance > 1 and val > root.right.item:
            return self.rotateLeft(root)
        elif balance > 1 and val < root.right.item:
            root.right = self.rotateRight(root.right)
            return self.rotateLeft(root)

        return root

    def search(self, root, val):

        if root == None:
            return False
        elif root.item == val:
            return True
        elif root.item < val:
            return self.search(root.right, val)
        else:
            return self.search(root.left, val)

    def get_height(self, root):
        if root == None:
            return 0
        else:
            return 1 + max(self.get_height(root.right), self.get_height(root.left))

    def get_balance(self, root):
        if root == None:
            return 0
        return self.get_height(root.right) - self.get_height(root.left)

    def rotateLeft(self, root):
        child = root.right
        root.right = child.left
        child.left = root

        child.height = 1 + max(self.get_height(child.left), self.get_height(child.right))
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        return child

    def rotateRight(self, root):
        child = root.left
        root.left = child.right
        child.right = root
        
        child.height = 1 + max(self.get_height(child.left), self.get_height(child.right))
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        return child

    def delete(self, root, val):

        if root == None:
            return root
        elif val < root.item:
            root.left = self.delete(root.left, val)
        elif val > root.item:
            root.right = self.delete(root.right, val)

        else:
            if root.right == None:
                temp = root.left
                root = None
                return temp
            elif root.left == None:
                temp = root.right
                root = None
                return temp

            new_root = self.get_minimum(root.right)
            root.item = new_root.item
            root.right = self.delete(root.right, new_root.item)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        balance = self.get_balance(root)

        if balance < -1 and self.get_balance(root.left) <= 0:
            return self.rotateRight(root)
        if balance < -1 and self.get_balance(root.left) > 0:
            root.left = self.rotateLeft(root.left)
            return self.rotateRight(root)
        if balance > 1 and self.get_balance(root.right) >= 0:
            return self.rotateLeft(root)
        if balance > 1 and self.get_balance(root.right) < 0:
            root.right = self.rotateRight(root.right)
            return self.rotateLeft(root)

        return root

            
          
    def get_minimum(self, root):
        if root.left == None:
            return root
        else:
            return self.get_minimum(root.left)

import re

def main():
    num = input("Enter the first number: ")
    root = AVLNode(num)
    tree = AVLTree()
    root.display()
    while True:
        num = input("Enter command: ")
        if num == 'bye':
            break
        else:
            m = re.search('(\w+)\s+(\d+)', num)
            command = m.group(1)
            number = m.group(2)
        if command == 'insert':
            root = tree.insert(root, number)
            root.display()
        elif command == 'delete':
            root = tree.delete(root, number)
            root.display()
        else:
            print("I don't understand ", command)
    

if __name__ == "__main__":
    main()
    

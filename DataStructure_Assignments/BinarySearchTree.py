"""
========================================
Dept. of Spanish Language and Literature
2012130730 Shim Jaeheon
Data Structure, Assignment #1
========================================
"""

with open('ex04.txt', 'r') as f:
    text = f.readlines()

class Node:
    def __init__(self, newval):
        self.val = newval
        self.left = None
        self.right = None
class BST:
    def __init__(self):
        self.root = None
    def insert(self,tree,n):
        if self.root is None:
            self.root = n
        elif n.val < tree.val:
            if tree.left is None:
                tree.left = n
            else:
                self.insert(tree.left,n)
        else:
            if tree.right is None:
                tree.right = n
            else:
                self.insert(tree.right,n)
    def writeInorder(self, tree, file):
        if tree is None:
            return
        else:
            self.writeInorder(tree.left, file)
            file.write(tree.val)
            self.writeInorder(tree.right, file)

def main():
    with open('assn02_out.txt', 'w') as out:
        bst = BST()
        for word in text:
            bst.insert(bst.root, Node(word))
        bst.writeInorder(bst.root, out)


"""
Sample run: 
assn02_out.txt

about
after
again
could
every
first
found
great
never
other
place
right
small
sound
still
their
there
these
think
those
three
under
water
where
which
words
would
write
years

"""
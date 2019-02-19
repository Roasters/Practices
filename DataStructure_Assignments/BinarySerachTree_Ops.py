"""
=========================================
 Dept. of Spanish Language and Literature
         2012130730 Shim Jaeheon
             Data Structure
             Assignment #3 
=========================================
"""

class Node:
    def __init__(self, newval):
        self.val = newval
        self.left = None
        self.right = None
        self.p = None
class BST:
    def __init__(self, wordList):
        self.root = None
        self.wordList = wordList[:]
        self.wordList.sort()
    def insert(self, tree, word):
        if self.root is None:
            self.root = word
        elif self.wordList.index(word.val) < self.wordList.index(tree.val):
            if tree.left is None:
                tree.left = word
                word.p = tree
            else:
                self.insert(tree.left,word)
        else:
            if tree.right is None:
                tree.right = word
                word.p = tree
            else:
                self.insert(tree.right,word)
    def search(self, tree, word):
        tmp = self.wordList[:] + [word]
        tmp.sort()
        if tree == None:
            print('The word "{}" doesn\'t exist.'.format(word))
            return None 
        elif word == tree.val:
            return tree
        if tmp.index(word) < tmp.index(tree.val):
            return self.search(tree.left, word)
        else:
            return self.search(tree.right, word)
    def minimum(self, tree):
        while tree.left != None:
            tree = tree.left
        return tree
    def maximum(self, tree):
        while tree.right != None:
            tree = tree.right
        return tree
    def transplant(self, tree, u, v):
        if u.p == None:
            tree = v
        elif u == u.p.left:
            u.p.left = v
        else:
            u.p.right = v
        if v != None:
            v.p = u.p
    def delete(self, tree, word):
        word = self.search(tree, word)
        if word == None:
            return None
        if word.left == None:
            self.transplant(tree, word, word.right)
        elif word.right == None:
            self.transplant(tree, word, word.left)
        else:
            tmp = self.minimum(word.right)
            if tmp.p != word:
                self.transplant(tree, tmp, tmp.right)
                tmp.right = word.right
                tmp.right.p = tmp
            if self.root == word:
                self.root = tmp
                tmp.p = None
            else:
                self.transplant(tree, word, tmp)
            tmp.left = word.left
            tmp.left.p = tmp
        print('The word "{}" is deleted'.format(word.val))

def makeTree():
    wordList = ['still', 'think', 'great', 'words', 'those', \
    'which', 'first', 'water', 'there', 'under', 'again', 'years', \
    'about', 'their', 'three', 'other', 'never', 'could', 'after', \
    'where', 'right', 'sound', 'small', 'write', 'would', 'found', \
    'every', 'these', 'place']
    global bst
    bst = BST(wordList)
    for word in wordList:
        bst.insert(bst.root, Node(word))

def whatToDelete():
    running = True
    while running:
        word = input('Enter the word to delete: ')
        bst.delete(bst.root, word)
        print(' ')
        answer = input('Want to delete more? [y/n]:')
        print(' ')
        if answer == 'n':
            running = False
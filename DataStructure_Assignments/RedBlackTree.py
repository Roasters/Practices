"""
=========================================
 Dept. of Spanish Language and Literature
         2012130730 Shim Jaeheon
             Data Structure
             Final Project
=========================================
"""

class Nil:
    def __init__(self):
        self.val = None
        self.c = 0   # color - 0: black | 1: red

class Node:
    def __init__(self, newval):
        self.val = newval
        self.left = Nil()
        self.right = Nil()
        self.p = Nil()
        self.c = None  
class RBT:
    def __init__(self, wordList):
        self.root = None
        self.wordList = wordList[:]
        self.wordList.sort()
    def insert(self, tree, word):
        tmpList = list(set(self.wordList[:] + [word.val]))
        tmpList.sort()
        if self.root is None:
            self.root = word
            word.c = 0
        elif tmpList.index(word.val) < tmpList.index(tree.val):
            if tree.left.val is None:
                tree.left = word
                word.p = tree
            else:
                self.insert(tree.left,word)
        else:
            if tree.right.val is None:
                tree.right = word
                word.p = tree
            else:
                self.insert(tree.right,word)
        word.c = 1
        self.RBInsertFixup(tree, word)
    def search(self, tree, word):
        tmp = list(set(self.wordList[:] + [word]))
        tmp.sort()
        if tree.val is None:
            return None 
        elif word == tree.val:
            return tree
        if tmp.index(word) < tmp.index(tree.val):
            return self.search(tree.left, word)
        else:
            return self.search(tree.right, word)
    def minimum(self, tree):
        while tree.left.val is not None:
            tree = tree.left
        return tree
    def maximum(self, tree):
        while tree.right.val is not None:
            tree = tree.right
        return tree
    def successor(self, tree, word):
        if word.right.val is not None:
            return self.minimum(word.right)
        tmp = word.p
        while tmp.val is not None and word == tmp.right:
            word = tmp
            tmp = tmp.p
        return tmp
    def predecessor(self, tree, word):
        if word.left.val is not None:
            return self.maximum(word.left)
        tmp = word.p
        while tmp.val is not None and word == tmp.left:
            word = tmp
            tmp = tmp.p
        return tmp
    def lRotate(self, tree, x):
        y = x.right
        x.right = y.left
        if y.left.val is not None:
            y.left.p = x
        y.p = x.p
        if x.p.val is None:
            self.root = y
        elif x == x.p.left:
            x.p.left = y
        else:
            x.p.right = y
        y.left = x
        x.p = y
    def rRotate(self, tree, x):
        y = x.left
        x.left = y.right
        if y.right.val is not None:
            y.right.p = x
        y.p = x.p
        if x.p.val is None:
            self.root = y
        elif x == x.p.right:
            x.p.right = y
        else:
            x.p.left = y
        y.right = x
        x.p = y
    def transplant(self, tree, u, v):
        if u.p.val is None:
            self.root = v
        elif u == u.p.left:
            u.p.left = v
        else:
            u.p.right = v
        if v.val is not None:
            v.p = u.p
    def delete(self, tree, word):
        word = self.search(tree, word)
        if word is None:
            return None
        tmp = word
        tmpOriginalColor = tmp.c
        if word.left.val is None:
            x = word.right
            self.transplant(tree, word, word.right)
        elif word.right.val is None:
            x = word.left
            self.transplant(tree, word, word.left)
        else:
            tmp = self.minimum(word.right)
            tmpOriginalColor = tmp.c
            x = tmp.right
            if tmp.p == word:
                x.p = tmp
            else:
                self.transplant(tree, tmp, tmp.right)
                tmp.right = word.right
                tmp.right.p = tmp
            self.transplant(tree, word, tmp)
            tmp.left = word.left
            tmp.left.p = tmp
            tmp.c = word.c
        if tmpOriginalColor == 0:
            self.RBDeleteFixup(tree, x)
        return 'dummy'
    def RBInsertFixup(self, tree, word):
        while word.p.c == 1:
            if word.p == word.p.p.left:
                tmp = word.p.p.right
                if tmp.c == 1:
                    word.p.c = 0
                    tmp.c = 0
                    word.p.p.c = 1
                    word = word.p.p
                elif word == word.p.right:
                    word = word.p
                    self.lRotate(tree, word)
                else:
                    word.p.c = 0
                    word.p.p.c = 1
                    self.rRotate(tree, word.p.p)
            else:
                tmp = word.p.p.left
                if tmp.c == 1:
                    word.p.c = 0
                    tmp.c = 0
                    word.p.p.c = 1
                    word = word.p.p
                elif word == word.p.left:
                    word = word.p
                    self.rRotate(tree, word)
                else:
                    word.p.c = 0
                    word.p.p.c = 1
                    self.lRotate(tree, word.p.p)
        self.root.c = 0
    def RBDeleteFixup(self, tree, word):
        while word != self.root and word.c == 0:
            if word == word.p.left:
                tmp = word.p.right
                if tmp.c == 1:
                    tmp.c = 0
                    word.p.c = 1
                    self.lRotate(tree, word.p)
                    tmp = word.p.right
                if tmp.left.c == 0 and tmp.right.c == 0:
                    tmp.color = 1
                    word = word.p
                elif tmp.right.c == 0:
                    tmp.left.c = 0
                    tmp.c = 1
                    self.rRotate(tree, tmp)
                    tmp = word.p.right
                else:
                    tmp.c = word.p.c
                    word.p.c = 0
                    tmp.right.c = 0
                    self.lRotate(tree, word.p)
                    word = self.root
            else:
                tmp = word.p.left
                if tmp.c == 1:
                    tmp.c = 0
                    word.p.c = 1
                    self.rRotate(word.p)
                    tmp = word.p.left
                if tmp.right.c == 0 and tmp.left.c == 0:
                    tmp.color = 1
                    word = word.p
                elif tmp.left.c == 0:
                    tmp.right.c = 0
                    tmp.c = 1
                    self.lRotate(tmp)
                    tmp = word.p.left
                else:
                    tmp.c = word.p.c
                    word.p.c = 0
                    tmp.left.c = 0
                    self.rRotate(word.p)
                    word = self.root
        word.c = 0

def makeTree():
    wordList = ['still', 'think', 'great', 'words', 'those', \
    'which', 'first', 'water', 'there', 'under', 'again', 'years', \
    'about', 'their', 'three', 'other', 'never', 'could', 'after', \
    'where', 'right', 'sound', 'small', 'write', 'would', 'found', \
    'every', 'these', 'place']
    global rbt
    rbt = RBT(wordList)
    for word in wordList:
        rbt.insert(rbt.root, Node(word))

with open('cmd.txt', 'r') as f:
    cmd = f.readlines()

def command(cmd):
    for line in cmd:
        line = line.strip()
        wordOriginal = rbt.search(rbt.root, line[-5:])
        if wordOriginal is None:
            rbt.insert(rbt.root, Node(line[-5:]))
        word = rbt.search(rbt.root, line[-5:])
        wordSuc = rbt.successor(rbt.root, word)
        wordPred = rbt.predecessor(rbt.root, word)
        if wordOriginal is None:
            dummy = rbt.delete(rbt.root, line[-5:])
        if wordSuc.val is None:
            wordSuc.val = 'Nil'
        if wordPred.val is None:
            wordPred.val = 'Nil'
        if line.startswith('-'):
            result = rbt.delete(rbt.root, line[-5:])
            if result is None:
                print(wordPred.val, 'NIL', wordSuc.val)
            else:
                print('The word "{}" is deleted'.format(line[-5:]))
        elif wordOriginal is None:
            print(wordPred.val, 'NIL', wordSuc.val)
        else:
            print(wordPred.val, wordOriginal.val, wordSuc.val)

"""
---------------------------------------- 
Dept. of Spanish Language and Literature
2012130730 Shim Jaeheon
Assignment #1
----------------------------------------
"""

# A given class that makes a linked list
class Node:
    def __init__(self):
        self.val = 0
        self.next = None

class List:
    def __init__(self):
        self.first = None
        self.y = []
    def insert_node(self, val):
        node = Node()
        node.val = val;
        node.next = self.first
        self.first = node
    def find(self, val):
        p = self.first
        while p is not None:
            if p.val == val:
                return p
            p = p.next;
        return None
    def print_list(self):
        p = self.first
        while p is not None:
            print(p.val)
            p = p.next;
        return None

# A class for making a reversed list 
class Reverse:
    def __init__(self):
        self.x = List()  # A linked list to store given data
        self.y = []      # A list to store reversely ordered data values

    def main(self, str_list):
        for str in str_list:
            self.x.insert_node(str)

    def pop(self):
        p = self.x.first
        while p is not None:
            self.y.append(p.val)  # Pop out the values from the lastly inserted one
            p = p.next
        return self.y    

# --------------------------------------------------------------------- #

# 1. Load word strings from a given file

data = open('ex04.txt', 'r')   # The file must be in the current working directory

words_list = [line for line in data.readlines()]  # A list in which the words from the file are stored

data.close()


# 2. Execute reversing statements

reverse = Reverse()
reverse.main(words_list)
reversed_list = reverse.pop()


# 3. Write in file the reversed version of the given word list

output = open('reversed.txt', 'w')

for word in reversed_list:
    if word[-1:] != '\n':
        output.write(word + '\n')
    else:
        output.write(word)

output.close()

"""
Sample run:
reversed.txt

under
never
those
found
small
every
still
again
great
sound
place
years
three
think
right
where
after
water
first
write
could
words
other
these
would
about
their
there
which
       
"""
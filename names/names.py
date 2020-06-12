import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    def __str__(self):
        print(f'{self.value}')

    # Insert the given value into the tree
    def insert(self, value):
        #compare the value to the root's value to determine which direction to go
        #if value < root's value, go left
        if value < self.value:
            #does it already have a left child though? We don't want to overwrite a value
            if self.left:
                #self.left is a Node
                self.left.insert(value)
            else:
                self.left = BSTNode(value)
        #otherwise value >=  root's value, go right
        else:
            if self.right:
                #self.right is a  Node
                self.right.insert(value)
            else:
                self.right = BSTNode(value)

    def contains(self, target):
        if target == self.value:
            return True
        elif target < self.value:
            if self.left:
                return self.left.contains(target)
            else:
                return False
        elif target > self.value:
            if self.right:
                return self.right.contains(target)
            else:
                return False

#hahaha record of hitting in 46 seconds 🙈

bst = BSTNode(names_1[0])
# print(bst)
for name in names_1:
    bst.insert(name)

for name2 in names_2:
    if bst.contains(name2):
        print('HITTING if')
        duplicates.append(name)

# for name in names_2:
#     if bst.contains(name):

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

import sys

class Node():
    def __init__(self, val):
        self.val = val
        self.parent = None
        self.left = None
        self.right = None
        self.color = 1  # 1-red 0-black


class RedBlackTree():
    def __init__(self):
        self.nil = Node(0)
        self.nil.color = 0
        self.nil.left = None
        self.nil.right = None
        self.root = self.nil

    def left_rotate(self, x): #LR
        y = x.right
        x.right = y.left
        if y.left != self.nil:
            y.left.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, x): #RR
        y = x.left
        x.left = y.right
        if y.right != self.nil:
            y.right.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def add_node(self, color, key):  #adding node but hardcoding its color(Zenoviy Veres said to do like that)
        node = Node(key)
        node.left = self.nil
        node.right = self.nil
        node.parent = None
        node.val = key
        node.color = color

        y = None
        x = self.root

        while x != self.nil:
            y = x
            if node.val < x.val:
                x = x.left
            else:
                x = x.right

        node.parent = y
        if y is None:
            self.root = node
        elif node.val < y.val:
            y.left = node
        else:
            y.right = node

        if node.parent == None:
            node.color = 0
            return f'{node.val} is root color is {node.color}'

        if node.parent is not None:
            return f'{node.val} parent is {node.parent.val} color is {node.color}'

    def __print_helper(self, node, indent, last): #basic tree print func that every rbtree uses
        if node != self.nil:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("R----")
                indent += "     "
            else:
                sys.stdout.write("L----")
                indent += "|    "

            s_color = "RED" if node.color == 1 else "BLACK"
            print(str(node.val) + "(" + s_color + ")")
            self.__print_helper(node.left, indent, False)
            self.__print_helper(node.right, indent, True)

    def blackDelete(self, x): #function 'blackDelete' is used to fix color problems, which appear after deleting black elem from tree
        while x != self.root and x.color == 0:

            if x == x.parent.left:
                sibling = x.parent.right

                if sibling.color == 1:
                    sibling.color = 0
                    x.parent.color = 1
                    self.left_rotate(x.parent)
                    sibling = x.parent.right

                if sibling.left.color == 0 and sibling.right.color == 0:
                    sibling.color = 1
                    x = x.parent
                else:
                    if sibling.right.color == 0:
                        sibling.left.color = 0
                        sibling.color = 1
                        self.right_rotate(sibling)
                        sibling = x.parent.right

                    sibling.color = x.parent.color
                    x.parent.color = 0
                    sibling.right.color = 0
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                sibling = x.parent.left
                if sibling.color == 1:
                    sibling.color = 0
                    x.parent.color = 1
                    self.right_rotate(x.parent)
                    sibling = x.parent.left

                if sibling.left.color == 0 and sibling.right.color == 0:
                    sibling.color = 1
                    x = x.parent
                else:
                    if sibling.left.color == 0:
                        sibling.right.color = 0
                        sibling.color = 1
                        self.left_rotate(sibling)
                        sibling = x.parent.left

                    sibling.color = x.parent.color
                    x.parent.color = 0
                    sibling.left.color = 0
                    self.right_rotate(x.parent)
                    x = self.root

        x.color = 0

    def transplant(self, u, v): #func to transplant two nodes of tree
        if u.parent == None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def delete_node_general(self, node, val): #func in which i delete node s in usual binary tree
                                              # and if color is black, call another function to fix it
        z = self.nil
        while node != self.nil:
            if node.val == val:
                z = node

            if node.val <= val:
                node = node.right
            else:
                node = node.left

        if z == self.nil:
            print("theres no such node here:)")
            return

        y = z
        y_color = y.color
        if z.left == self.nil:
            x = z.right
            self.transplant(z, z.right)
        elif (z.right == self.nil):
            x = z.left
            self.transplant(z, z.left)
        else:
            y = self.RBminimum(z.right)
            y_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.parent = y

            self.transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if y_color == 0:
            self.blackDelete(x)

    def RBdelete_node(self, val): #func to be comfortable to call 'delete general' out of class
        self.delete_node_general(self.root, val)

    def RBminimum(self, node): #just going down the tree to find min val
        while node.left != self.nil:
            node = node.left
        return node

    def RBprint_tree(self): #func to be comfortable to call 'print' put of class
        self.__print_helper(self.root, "", True)


rb = RedBlackTree()

rb.add_node(0, 34)
rb.add_node(0, 67)
rb.add_node(1, 22)
rb.add_node(0, 24)
rb.add_node(0, 17)
rb.add_node(1, 20)
rb.add_node(1, 16)

rb.RBprint_tree()

rb.RBdelete_node(17)

rb.RBprint_tree()
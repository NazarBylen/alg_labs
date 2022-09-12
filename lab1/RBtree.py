import sys

class Node:
    """
        1-red
        0-black
    """
    def __init__(self, val):
        self.val = val
        self.parent = None
        self.left = None
        self.right = None
        self.color = 1


class RedBlackTree:
    def __init__(self):
        self.nil = Node(0)
        self.nil.color = 0
        self.nil.left = None
        self.nil.right = None
        self.root = self.nil

    def left_rotate(self, rotate_node):
        """"
            Left-Rotate
        """
        rotate_child = rotate_node.right
        rotate_node.right = rotate_child.left
        if rotate_child.left is not self.nil:
            rotate_child.left.parent = rotate_node

        rotate_child.parent = rotate_node.parent
        if rotate_node.parent is None:
            self.root = rotate_child
        elif rotate_node is rotate_node.parent.left:
            rotate_node.parent.left = rotate_child
        else:
            rotate_node.parent.right = rotate_child
        rotate_child.left = rotate_node
        rotate_node.parent = rotate_child

    def right_rotate(self, rotate_node):
        """"
            Right-Rotate
        """
        rotate_child = rotate_node.left
        rotate_node.left = rotate_child.right
        if rotate_child.right is not self.nil:
            rotate_child.right.parent = rotate_node

        rotate_child.parent = rotate_node.parent
        if rotate_node.parent is None:
            self.root = rotate_child
        elif rotate_node is rotate_node.parent.right:
            rotate_node.parent.right = rotate_child
        else:
            rotate_node.parent.left = rotate_child
        rotate_child.right = rotate_node
        rotate_node.parent = rotate_child

    def add_node(self, color, key):
        """
            adding node but hardcoding its color(Zenoviy Veres said to do like that)
        """
        node = Node(key)
        node.left = self.nil
        node.right = self.nil
        node.parent = None
        node.val = key
        node.color = color

        y = None
        node_iterator = self.root

        while node_iterator is not self.nil:
            y = node_iterator
            if node.val < node_iterator.val:
                node_iterator = node_iterator.left
            else:
                node_iterator = node_iterator.right

        node.parent = y
        if y is None:
            self.root = node
        elif node.val < y.val:
            y.left = node
        else:
            y.right = node

        if node.parent is None:
            node.color = 0
            return f'{node.val} is root color is {node.color}'

        if node.parent is not None:
            return f'{node.val} parent is {node.parent.val} color is {node.color}'

    def __print_helper(self, node, indent, last):
        """
            basic tree print func that every rbtree uses
        """
        if node is not self.nil:
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

    def black_delete(self, del_child):
        """
            function 'blackDelete' is used to fix color problems, which appear after deleting black elem from tree
        """
        while del_child is not self.root and del_child.color == 0:

            if del_child is del_child.parent.left:
                sibling = del_child.parent.right

                if sibling.color == 1:
                    sibling.color = 0
                    del_child.parent.color = 1
                    self.left_rotate(del_child.parent)
                    sibling = del_child.parent.right

                if sibling.left.color == 0 and sibling.right.color == 0:
                    sibling.color = 1
                    del_child = del_child.parent
                else:
                    if sibling.right.color == 0:
                        sibling.left.color = 0
                        sibling.color = 1
                        self.right_rotate(sibling)
                        sibling = del_child.parent.right

                    sibling.color = del_child.parent.color
                    del_child.parent.color = 0
                    sibling.right.color = 0
                    self.left_rotate(del_child.parent)
                    del_child = self.root
            else:
                sibling = del_child.parent.left
                if sibling.color == 1:
                    sibling.color = 0
                    del_child.parent.color = 1
                    self.right_rotate(del_child.parent)
                    sibling = del_child.parent.left

                if sibling.left.color == 0 and sibling.right.color == 0:
                    sibling.color = 1
                    del_child = del_child.parent
                else:
                    if sibling.left.color == 0:
                        sibling.right.color = 0
                        sibling.color = 1
                        self.left_rotate(sibling)
                        sibling = del_child.parent.left

                    sibling.color = del_child.parent.color
                    del_child.parent.color = 0
                    sibling.left.color = 0
                    self.right_rotate(del_child.parent)
                    del_child = self.root

        del_child.color = 0

    def transplant(self, parent, child):
        """"
            func to transplant two nodes of tree
        """
        if parent.parent is None:
            self.root = child
        elif parent is parent.parent.left:
            parent.parent.left = child
        else:
            parent.parent.right = child
        child.parent = parent.parent

    def delete_node(self, node, val):
        """"
            func in which i delete node s in usual binary tree
            and if color is black, call another function to fix it
        """
        node_to_delete = self.nil
        while node is not self.nil:
            if node.val is val:
                node_to_delete = node

            if node.val <= val:
                node = node.right
            else:
                node = node.left

        if node_to_delete is self.nil:
            print("theres no such node here:)")
            return

        node_to_delete_analog = node_to_delete
        new_color = node_to_delete_analog.color
        if node_to_delete.left is self.nil:
            del_child = node_to_delete.right
            self.transplant(node_to_delete, node_to_delete.right)
        elif node_to_delete.right is self.nil:
            del_child = node_to_delete.left
            self.transplant(node_to_delete, node_to_delete.left)
        else:
            node_to_delete_analog = self.rb_minimum(node_to_delete.right)
            new_color = node_to_delete_analog.color
            del_child = node_to_delete_analog.right
            if node_to_delete_analog.parent is node_to_delete:
                del_child.parent = node_to_delete_analog
            else:
                self.transplant(node_to_delete_analog, node_to_delete_analog.right)
                node_to_delete_analog.right = node_to_delete.right
                node_to_delete_analog.right.parent = node_to_delete_analog

            self.transplant(node_to_delete, node_to_delete_analog)
            node_to_delete_analog.left = node_to_delete.left
            node_to_delete_analog.left.parent = node_to_delete_analog
            node_to_delete_analog.color = node_to_delete.color
        if new_color == 0:
            self.black_delete(del_child)

    def rb_delete_node(self, val):
        """
            func to be comfortable to call 'delete general' out of class
        """
        self.delete_node(self.root, val)

    def rb_minimum(self, node):
        """
            just going down the tree to find min val
        """
        while node.left != self.nil:
            node = node.left
        return node

    def rb_print_tree(self):
        """"
            func to be comfortable to call 'print' put of class
        """
        self.__print_helper(self.root, "", True)


rb = RedBlackTree()

rb.add_node(0, 34)
rb.add_node(0, 67)
rb.add_node(1, 22)
rb.add_node(0, 24)
rb.add_node(0, 17)
rb.add_node(1, 20)
rb.add_node(1, 16)

rb.rb_print_tree()

rb.rb_delete_node(20)

rb.rb_print_tree()
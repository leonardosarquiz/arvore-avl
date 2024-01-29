import sys

lines = []

for line in sys.stdin:
    if 'Exit' == line.rstrip():
        break
    lines.append(line.split('\n')[0])


initial_tree = [int(x) for x in lines[1].split(' ')]
new_element = int(lines[2])


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def __init__(self):
        self.root = None

    def print_in_order(self, node):
        if node is not None:
            self.print_in_order(node.left)
            print(f"{node.value}(BF={self.get_balance(node)})", end=" ")
            self.print_in_order(node.right)

    def print_post_order(self, node):
        if node is not None:
            print(f"{node.value}(BF={self.get_balance(node)})", end=" ")
            self.print_post_order(node.left)
            self.print_post_order(node.right)

    def print(self):
        self.print_in_order(self.root)
        print("")
        self.print_post_order(self.root)

    def insert(self, value):
        self.root = self._insert(self.root, value)

    def _insert(self, node, value):
        if node is None:
            return Node(value)
        elif value < node.value:
            node.left = self._insert(node.left, value)
        elif value > node.value:
            node.right = self._insert(node.right, value)
        else:
            return self.root

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        
        # Rotação simples a direita
        balance = self.get_balance(node)
        if balance > 1 and value < node.left.value:
            return self.rotate_right(node)
        # Rotação simples à esquerda
        if balance < -1 and value > node.right.value:
            return self.rotate_left(node)
        # Rotação dupla à esquerda depois à direita
        if balance > 1 and node.left.value < value:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)
         # Rotação dupla à direita depois à esquerda
        if balance < -1 and node.right.value > value:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node

    def rotate_left(self, node):
        node_right = node.right
        left_of_node_right = node_right.left

        node_right.left = node
        node.right = left_of_node_right

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        node_right.height = 1 + max(self.get_height(node_right.left), self.get_height(node_right.right))
        return node_right

    def rotate_right(self, node):
        left_of_node = node.left
        right_of_left_of_node = left_of_node.right

        left_of_node.right = node
        node.left = right_of_left_of_node
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        left_of_node.height = 1 + max(self.get_height(left_of_node.left), self.get_height(left_of_node.right))
        return left_of_node

    def get_balance(self, node):
        if node is None:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def get_height(self, root):
        if root is None:
            return 0
        else:
            return root.height


tree = AVLTree()
for sample in initial_tree:
    tree.insert(sample)

tree.insert(new_element)
tree.print()

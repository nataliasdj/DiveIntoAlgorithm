class Node:
    def __init__(self,value,left = None, right = None):
        self.value = value
        self.left = left
        self.right = right
    def __str__(self):
        return "Node(" + str(self.value) + ")"
def dfs_recursive(root): 
    if root is not None:
        print(root)
    dfs_recursive(root.left)
    dfs_recursive(root.right)

def dfs_interative(root, stack):
    stack.append(root)
    while len(stack) > 0:
        node = stack.pop()
        if node is not None:
            print(node)
            stack.append(node.left)
            stack.append(node.right)

def bfs(queue, root):
    queue.append(root)
    while queue:
        node = queue.pop(0) #popleft
        if node is not None:
            print(node)
            queue.append(node.left)
            queue.append(node.right)
example_tree = Node('A',Node('B', Node('D'), Node('E')), Node('C', Node('F'), Node('G')))
my_queue = []
bfs(my_queue,example_tree)
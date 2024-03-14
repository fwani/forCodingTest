import sys


def pre_traversal(node):
    if node != '.':
        print(node, end='')
        pre_traversal(tree[node][0])  # left
        pre_traversal(tree[node][1])  # right


def mid_traversal(node):
    if node != '.':
        mid_traversal(tree[node][0])  # left
        print(node, end='')
        mid_traversal(tree[node][1])  # right


def post_traversal(node):
    if node != '.':
        post_traversal(tree[node][0])  # left
        post_traversal(tree[node][1])  # right
        print(node, end='')


node_count = int(sys.stdin.readline().strip())
tree = {}
for _ in range(node_count):
    now, left, right = sys.stdin.readline().strip().split(" ")
    tree[now] = (left, right)
pre_traversal('A')
print()
mid_traversal('A')
print()
post_traversal('A')
print()

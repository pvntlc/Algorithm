# 1991번 : 트리 순회 – Silver 1
import sys
input = sys.stdin.readline

n = int(input())
n_list = {}

for _ in range(n):
    Root, Left, Right = input().split()
    n_list[Root] = [Left, Right]

def preorder(root):
    if root != '.':
        print(root, end="")
        preorder(n_list[root][0])
        preorder(n_list[root][1])

def inorder(root):
    if root != '.':
        inorder(n_list[root][0])
        print(root, end="")
        inorder(n_list[root][1])

def postorder(root):
    if root != '.':
        postorder(n_list[root][0])
        postorder(n_list[root][1])
        print(root, end="")

preorder('A')
print()
inorder('A')
print()
postorder('A')
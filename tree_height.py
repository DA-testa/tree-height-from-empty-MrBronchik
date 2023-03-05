#python3

import sys
import threading
import os

def compute_height(n, parents):
    children = {i: [] for i in range(n)}

    root = None
    for i in range(n):
        parent = parents[i]
        if parent == -1:
            root = i
        else:
            children[parent].append(i)

    def height(node):
        if not children[node]:
            return 1
        else:
            return 1 + max(height(child) for child in children[node])
    return height(root)

def main():
    text = input()
    if "I" in text:
        n = int(input())
        parents = list(map(int, input().split()))
    elif "F" in text:

        path = "./test/"

        filename = input("Enter the file name: ")

        file_path = os.path.join(path, filename)

        if "a" not in filename:
            try:
                with open(file_path) as f:
                    n = int(f.readline().strip())
                    parents = list(map(int, f.readline().strip().split()))
            except Exception as e:
                print("Error:", str(e))
                return

    else:
        print("Enter 'I' or 'F':")
        return

    print(compute_height(n, parents))

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()

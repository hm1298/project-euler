#hm1289, solution from 2022
#definitely need to clean this up in the future
import time
from collections import deque

def solve():
    """
    .
    """
    ans, root = 0, populate(5)

    #print(root.children)

    queue = deque([root])
    while queue:
        node = queue.popleft()
        for v, p in node.children:
            v.val += p * node.val
            if v not in queue:
                queue.append(v)
        if node.state == [1, 0, 0, 0, 0]:
            ans = node.val
    return ans - 2

class Tree:
    def __init__(self, val, state, children=None):
        self.val = val
        self.state = state
        self.children = [] if not children else children
        #children have form [node, edge weight]

def populate(n=5):
    """
    """
    x = [1] + [0] * (n - 1)
    antiroot = Tree(1, x)
    queue, vertices = deque([antiroot]), {tuple(antiroot.state): antiroot}
    while queue:
        node = queue.popleft()

        #print("Selecting new node from queue: " + str(node.state))

        denom = sum(node.state)
        for i in range(n):
            #print("Checking " + str(i) + "th index of " + str(node.state))
            num = node.state[i]
            if num > 0:
                new_state = cut_in_half(node.state, i)
                #print("Found a match. " + str(node.state) + " has parent " + str(new_state))
                key = tuple(new_state)
                if key not in vertices:
                    #print(str(new_state) + " has not been seen before. Adding it to the vertices.")
                    if sum(new_state) == 1:
                        vertices[key] = Tree(1, new_state)
                    else:
                        vertices[key] = Tree(0, new_state)
                    #print(str(new_state) + " has not been in queue before. Adding to queue.")
                    queue.append(vertices[key])
                #print("Now adding " + str(node.state) + " as child of " + str(vertices[key].state))
                vertices[key].children.append([node, num / denom])

    end_state = [0] * n
    ans = vertices[tuple(end_state)]

    #for key in vertices:
    #    print(key)
    #print("break for this many children of root: " + str(len(ans.children)))
    #for child in ans.children:
    #    print(child[0].state)
    return ans

def cut_in_half(arr, i):
    assert arr[i] > 0
    return arr[:i] + [arr[i] - 1] + [k + 1 for k in arr[i + 1:]]

start = time.time()
print("{:0.6f}".format(solve()))
print("Elapsed time: {:0.4f}".format(time.time() - start))
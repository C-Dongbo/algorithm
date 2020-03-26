from collections import deque
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children



class Solution:
  def levelOrder(self, root: Node) :
    if root is None:
      return []

    result = []
    queue = deque()
    queue.append(root)

    while queue:
      same_level = []
      for i in range(len(queue)):
        node = queue.popleft()
        same_level.append(node.val)
        if node.children is not None:
          for child in node.children:
            if child:
              queue.append(child)
      result.append(same_level)
    return result


if __name__ =='__main__':
  test = Node(1,[Node(3,[Node(5),Node(6)]),Node(2),Node(4)])
  Solution = Solution()
  print(Solution.levelOrder(test))
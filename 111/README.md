# 111. Minimum Depth of Binary Tree

## General explanation of Solution

So in this question leetcode is asking us to find the minimum depth of a tree, that is the shortest avilable path between the root node and a leaf node with no child nodes. As you can see in the solution, we've used recursion to solve this one which has the added benefit of keeping the code compact but it can be a bit confusing. As always this isn't the only possible answer and this one could be optomized more if you'd like.

__One thing we found confusing while doing this problem is the defenition of depth. I've always been taught you count the number of edges when calculating depth or height but while working on this problem found that there isn't one standard defenition. In this question they count the number of nodes so keep that in mind when working on the solution.__

We'll take a look at the use case provided as part of the question so that you can follow along!

    3
   / \
  9  20
    /  \
   15   7

Now how does this code work? Well first let's take a look at the TreeNode class provided by Leetcode:

```
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
```

Every node consists of a val (the value of the node we are currently looking at), a left (the value of the node on the left if there is one), and a right (the value of the node on the right if it has one). If there is no node to the left or right the value is None or Null. And that's pretty much it! What we need to keep in mind while traversing these nodes is there are 3 possibilities:

l. The node has no value, it's none
l. The node has a single child, either left or right
l. The node has 2 children
l. The node has no children

So to start here is the whole method:

```
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        if not root.left or not root.right:
            return 1+(max(self.minDepth(root.left), self.minDepth(root.right)))
        return 1+(min(self.minDepth(root.left), self.minDepth(root.right)))
```

So what are we trying to do with each portion of the code?

```
if not root:
    return 0
```

So the first part is maybe the easiest to understand. If the value of the node we are looking at is None, return a 0. This doesn't count as a node and shouldn't add to our final count. Next!

```
if not root.left or not root.right:
    return 1+(max(self.minDepth(root.left), self.minDepth(root.right)))
```

Here we are checking to see if the node has at least ONE child. So long as one of the children is None, we'll take that node and get the max of it's 2 children. And return that value +1 . Now we are sending the left and right values through the method we are already in. This is important but I want to go over the last part first and then I'll explain why so hold tight.

```
return 1+(min(self.minDepth(root.left), self.minDepth(root.right)))
```

None of the other conditions are met return the minimum of those 2 child nodes +1 . Straight forwared right? 

But how does this calculate the depth?


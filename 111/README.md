# 111. Minimum Depth of Binary Tree

## General explanation of Solution

So in this question leetcode is asking us to find the minimum depth of a tree, that is the shortest avilable path between the root node and a leaf node with no child nodes. As you can see in the solution, we've used recursion to solve this one which has the added benefit of keeping the code compact but it can be a bit confusing. As always this isn't the only possible answer and this one could be optomized more if you'd like.

__One thing we found confusing while doing this problem is the defenition of depth. I've always been taught you count the number of edges when calculating depth or height but while working on this problem found that there isn't one standard defenition. In this question they count the number of nodes so keep that in mind when working on the solution.__

We'll take a look at the use case provided as part of the question so that you can follow along!

```
    3
   / \
  9  20
    /  \
   15   7
```

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

But how does this calculate the depth though? Let's take a look at the min and max functions:

```
return 1+(max(self.minDepth(root.left), self.minDepth(root.right)))
...
return 1+(min(self.minDepth(root.left), self.minDepth(root.right)))
```

Notice something? We're taking each of the nodes and sending them through the function we are already in! Why do that? Well the logic will be the same for processing every node, there isn't really a need for the nodes to be processed differently since they all fit the same criteria. You may also have looked at the code earlier and asked yourself, how are we tracking the node count as we go down? We aren't storing any variables. So let's just walk through it shall we?

```
			      ->    3
				   / \
				  9  20
				    /  \
				   15   7
```

So we start at 3. The root isn't None, so we don't return 0. Also, neither the left or right are none. So we go to the default which is the min + 1 of the left and right. But first we have to evaluate the left and right nodes by sending them through the minDepth function. So.....

```
				    3
				   / \
			      ->  9  20
				    /  \
				   15   7
```

If we look at node 9 we see that both the left and right are None. So we hit our second condition ( where at least left or right is None) and we take the max those two values. But since both of those legs are None, they return 0. So the max of 0 and 0 is 0. But wait, we return max + 1. So back at our original call at node 3 we have 1 + min(1, minDepth(20)). So now we gotta evaluate the other half of the tree to make sure there isn't a shorter path available right? 

```
			            3
				   / \
				  9  20    <-
				    /  \
				   15   7
```

So now we evaluate 20. Same deal as 3, both left and right are not none. So let's drop down again and we will evaluate from left to right.

```
			            3
				   / \
				  9  20
				    /  \
			      ->   15   7
```

Alright so 15 doesn't have any children, so they both return 0 and the max of that is 0 + 1. So at node 20 we are at 1 + min(1, minDepth(7)), let's evalutate 7. 

```

			            3
				   / \
				  9  20
				    /  \
			           15   7  <-
```

7 is the same as 15, no children. We end up returning 1. So back at node 20 we have 1 + min (1, 1) which gives us 1 + 1 meaning we return 2 to the waiting min call at node 3. Hang in there, we're almost done!

```
			      ->    3
				   / \
				  9  20
				    /  \
				   15   7
```

Now we're back where we started with 1 + min(1,2) which resolves to 1 + 1 meaning we return 2. Which, for this example means we've returned the correct answer! If you're still having trouble following along, I recommend drawing it out on a piece of paper or whiteboard. That helped us work through this a ton. Good luck with your own implementation! 

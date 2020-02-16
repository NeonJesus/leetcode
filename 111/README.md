# 111. Minimum Depth of Binary Tree

## General explanation of Solution

So in this question leetcode is asking us to find the minimum depth of a tree, that is the shortest avilable path between the root node and a leaf node with no child nodes. As you can see in the solution, we've used recursion to solve this one which has the added benefit of keeping the code compact but it can be a bit confusing. As always this isn't the only possible answer and this one could be optomized more if you'd like.

__One thing we found confusing while doing this problem is the defenition of depth. I've always been taught you count the number of edges when calculating depth or height but while working on this problem found that there isn't one standard defenition. In this question they count the number of nodes so keep that in mind when working on the solution.__



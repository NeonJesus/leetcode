"""Given an integer number n, return the difference between the product of its digits and the sum of its digits."""

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        prod=1
        total=0
    
        while n!=0:
            num=n%10
            prod=prod*num
            total=total+num
            n=n//10
        return prod-total

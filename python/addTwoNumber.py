class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        current, carry = dummy, 0
        
        while l1 or l2:
            val = carry
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
            carry, val = val / 10, val % 10
            current.next = ListNode(val)
            current = current.next
        result=[]
        if carry == 1:
            current.next = ListNode(1)
        result=[dummy.next.val,dummy.next.next.val,dummy.next.next.next.val]
        return result
def makeNums(nums):
    re=[]
    for i in nums:
        re.append(int(i))
    return re
if __name__ == '__main__':
    z=input()
    z=makeNums(z)
    x=input()
    x=makeNums(x)
    a, a.next, a.next.next = ListNode(z[0]), ListNode(z[1]), ListNode(z[2])
    b, b.next, b.next.next = ListNode(x[0]), ListNode(x[1]), ListNode(x[2])
    result = Solution().addTwoNumbers(a, b)
    print result
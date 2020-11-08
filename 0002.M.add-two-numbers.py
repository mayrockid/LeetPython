# 2. 两数相加
# https://leetcode-cn.com/problems/add-two-numbers/

#Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def adding(l1: ListNode, l2: ListNode, carry: int) -> ListNode:
            _node = ListNode()
            l1_val = l1.val if l1 else 0
            l1_next = l1.next if l1 else None
            l2_val = l2.val if l2 else 0
            l2_next = l2.next if l2 else None
            a, b = divmod(l1_val + l2_val + carry, 10)

            _node.val = b
            if l1_next or l2_next or a:
                _node.next = adding(l1_next, l2_next, a)
            return _node

        return adding(l1, l2, 0)


def list2node(l: List[int]) -> ListNode:
    ln = ListNode()
    lnn = ln
    for v in l:
        lnn.next = ListNode(val=v)
        lnn = lnn.next
    return ln.next


def node2string(ln: ListNode) -> str:
    s = ""
    s += str(ln.val)
    if ln.next:
        s += " -> "
        s += node2string(ln.next)
    return s


testcase = [
    ([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9]),
    ([2, 4, 3], [5, 6, 4]),
]

if __name__ == "__main__":
    obj = Solution()
    for l1, l2 in testcase:
        ln1 = list2node(l1)
        print(node2string(ln1))

        ln2 = list2node(l2)
        print(node2string(ln2))

        lnSum = obj.addTwoNumbers(ln1, ln2)
        print(node2string(lnSum))
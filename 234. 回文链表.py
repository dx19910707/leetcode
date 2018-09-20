# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        92ms beats: 95.13%
        """
        vals = []
        while head:
            vals.append(head.val)
            head = head.next
        return vals == vals[::-1]

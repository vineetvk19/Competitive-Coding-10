# Time-Complexity: O(1) for every function
# Space Complexity: O(1)
# Leetcode status: Accepted


# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator(object):
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator(object):
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iter = iterator
        self.peeked = False
        self.temp = None
        

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if self.peeked:
            return self.temp
        self.peeked = True
        self.temp = self.iter.next()
        return self.temp

    def next(self):
        """
        :rtype: int
        """
        if self.peeked:
            self.peeked = False
            return self.temp
        return self.iter.next()
        

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.peeked or self.iter.hasNext():
            return True
        return False
        

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the  next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].

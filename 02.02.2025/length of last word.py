class Solution(object):
    def lengthOfLastWord(self, s):
        y=s.split()
        return len(y[-1])

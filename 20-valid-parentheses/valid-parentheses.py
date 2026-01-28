class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        
        bracket_map = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        
        for ch in s:
           
            if ch in bracket_map.values():
                stack.append(ch)
            else:
               
                if not stack or stack[-1] != bracket_map[ch]:
                    return False
                stack.pop()
        
        return not stack

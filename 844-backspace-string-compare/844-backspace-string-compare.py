class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def back(string):
            stack = []
            for ch in string:
                if ch != '#':stack.append(ch)
                elif stack:stack.pop()
            return stack
        return back(s) == back(t)
    
    # time complexity: O(M+N)
    # space complexity: O(M+N)
    
if __name__ == '__main__':
    s = Solution()
    assert True == s.backspaceCompare(s = "ab#c", t = "ad#c")
    assert True == s.backspaceCompare(s = "ab##", t = "c#d#")
    assert False == s.backspaceCompare(s = "a#c", t = "b")
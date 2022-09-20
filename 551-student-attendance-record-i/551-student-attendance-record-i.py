class Solution:
    def checkRecord(self, s: str) -> bool:
        return False if 'LLL' in s else s.count('A') < 2
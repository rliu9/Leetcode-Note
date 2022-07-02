class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        res = set()
        hashtable = defaultdict(int)
        for i in range(9, len(s)):
            hashtable[s[i-9:i+1]] += 1
        for key,value in hashtable.items():
            if value >= 2:
                res.add(key)
        return list(res)
    
    # Time Complexity: (N-10)10 -> slicing:10; for loop: N-10
    # Space Complexity: (N-10)10
    
if __name__ == '__main__':
    s = Solution()
    #assert ["AAAAACCCCC","CCCCCAAAAA"] == sorted(s.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))
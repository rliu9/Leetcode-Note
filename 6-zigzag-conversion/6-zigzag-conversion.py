class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:return s
        hashmap = collections.defaultdict(list)
        depth, i = 0, 0
        while i < len(s):
            while i < len(s) and depth < numRows-1:
                hashmap[depth].append(s[i])
                depth += 1
                i += 1
            while i < len(s) and depth > 0:
                hashmap[depth].append(s[i])
                depth -= 1
                i += 1
        return ''.join([ele for sub in hashmap.values() for ele in sub])
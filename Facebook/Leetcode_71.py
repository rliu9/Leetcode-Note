class Solution:
    def simplifyPath(self, path: str) -> str:
        s = path.split('/')
        res = []
        for i in s:
            if i == '..': 
                if res: res.pop()
                if res: res.pop()
            elif i == '.': continue
            elif i and '/' not in i:
                res.append(i)
                res.append('/')
        res.insert(0, '/')
        if res and len(res) != 1 and res[-1] == '/': res.pop()
        return ''.join(res)

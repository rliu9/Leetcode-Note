class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        buffer = []
        for s in strs:buffer += [chr(len(s)), s]
        return ''.join(buffer)
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        i, n, res = 0, len(s), []
        while i < n:
            len_str = ord(s[i])
            i += 1
            if len_str + i > n:break
            res.append(s[i:i+len_str])
            i += len_str
        return res


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
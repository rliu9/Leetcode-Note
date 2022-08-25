class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        buffer = []
        for s in strs:
            buffer += [chr(len(s)), s]
        return ''.join(buffer)
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        res = []
        pos = 0
        while pos < len(s):
            str_len = ord(s[pos])
            pos += 1
            if pos + str_len > len(s):
                return
            res.append(s[pos:pos + str_len])
            pos += str_len
        return res


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
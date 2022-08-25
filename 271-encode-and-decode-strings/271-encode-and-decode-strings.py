class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        buffer = []
        for i, s in enumerate(strs):
            if i == 0:buffer+=[s]
            else:buffer += ['.hardtoguest.', s]
        return ''.join(buffer)
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        return s.split('.hardtoguest.')


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
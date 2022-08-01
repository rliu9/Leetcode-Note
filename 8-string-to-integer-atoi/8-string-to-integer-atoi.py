class Solution:
    def myAtoi(self, s: str) -> int:
        regex = r"\s*([+-]?)(\d+)"
        match = re.match(regex, s)
        value = 0
        if match:
            value = (min(2**31-1, int(match.group(2))) if match.group(1) != '-' else max(-1*int(match.group(2)),-2**31))
        return value
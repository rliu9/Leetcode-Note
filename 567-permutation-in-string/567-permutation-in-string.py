class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter, k = collections.Counter(s1), len(s1)
        for i in range(len(s2)):
            if counter == collections.Counter(s2[i:i+k]):return True
        return False
    
    # O(n k^2)
    # O(1) because counter only contains at most 26 key-value pairs
    
    
    
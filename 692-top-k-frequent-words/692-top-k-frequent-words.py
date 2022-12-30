class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        cnt = Counter(words)
        return nsmallest(k, cnt.keys(), key=lambda x: (-cnt[x], x))
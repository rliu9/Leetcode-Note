class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        pair_sum = 2 * sum(skill)//len(skill)
        chemistry = 0
        c = collections.Counter(skill)
        for key,value in c.items():
            if value != c[pair_sum-key]:
                return -1
            chemistry += key * value * (pair_sum-key)
        return chemistry//2
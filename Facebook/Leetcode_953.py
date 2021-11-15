class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        for i, j in zip(words, words[1:]):
            len_i,len_j = len(i), len(j)
            index_i, index_j = 0, 0
            while index_i < len_i and index_j < len_j:
                order_i = order.index(i[index_i])
                order_j = order.index(j[index_j])
                if order_i < order_j:
                    break
                elif order_i > order_j:
                    return False
                else:
                    index_i += 1
                    index_j += 1
            if index_i < len_i and index_j == len_j: return False
        return True

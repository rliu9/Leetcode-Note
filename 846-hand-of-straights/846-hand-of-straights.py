class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # greedy
        hand.sort()
        c = collections.Counter(hand)
        while hand:
            temp = hand[0]
            for _ in range(groupSize):
                if c[temp] <= 0:return False
                hand.remove(temp)
                c[temp] -= 1
                temp += 1
        return True
    
    # O(nlogn)
    # O(n)
                
                
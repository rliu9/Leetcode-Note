class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        #if 2*groupSize > len(hand):return False
        hand.sort()
        d = Counter(hand)
        while len(hand) != 0:
            temp = hand[0]
            for _ in range(groupSize):
                if temp not in d:return False
                d[temp] -= 1
                hand.remove(temp)
                if d[temp] == 0: del d[temp]
                temp += 1
        return True
                
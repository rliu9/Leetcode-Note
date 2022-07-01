class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        move = 0
        for direction, moves in shift:
            if direction == 0:
                move += moves
            else:
                move -= moves
        move %= len(s)
        return s[move:] + s[:move]
                
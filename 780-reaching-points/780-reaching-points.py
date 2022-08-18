class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        if tx<sx or ty<sy:
            return False
        if sx == tx:
            return ((ty - sy) % sx) == 0
        elif sy == ty:
            return ((tx - sx) % sy) == 0
        
        if tx > ty:
            return self.reachingPoints(sx, sy, tx%ty, ty)
        else:
            return self.reachingPoints(sx, sy, tx, ty%tx)
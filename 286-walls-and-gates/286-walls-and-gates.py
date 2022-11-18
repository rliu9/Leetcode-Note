class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        row, col = len(rooms), len(rooms[0])
        q, seen = deque([]), set()
        def addRoom(r,c):
            if 0 <= r < row and 0 <= c < col and (r,c) not in seen and rooms[r][c] != -1:
                q.append((r,c))
                seen.add((r,c))
        for r in range(row):
            for c in range(col):
                if rooms[r][c] == 0:
                    q.append((r,c))
                    seen.add((r,c))
        dist = 0
        while q:
            for _ in range(len(q)):
                x, y = q.popleft()
                rooms[x][y] = dist
                addRoom(x+1, y)
                addRoom(x-1, y)
                addRoom(x, y+1)
                addRoom(x, y-1)
            dist += 1
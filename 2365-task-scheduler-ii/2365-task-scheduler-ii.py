class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        ret = 0
        wait = {t: -1 for t in tasks}
        for i,task in enumerate(tasks):
            w = wait[task]
            if w > ret:ret = w 
            wait[task] = ret + space + 1
            ret += 1
        return ret
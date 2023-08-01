class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        adj = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                h = word[:i]+'#'+word[i+1:]
                adj[h].append(word)
        parents = defaultdict(set)  
        q = deque([(beginWord,0)])
        seen = {beginWord:0}
        minDist = float('inf')
        while q:
            word,dist = q.popleft()
            for i in range(len(word)):
                h = word[:i]+'#'+word[i+1:]
                for neighbor in adj[h]:
                    if neighbor not in seen or seen[neighbor]==dist+1<=minDist:
                        if neighbor==endWord:minDist = dist+1
                        parents[neighbor].add(word)
                        if neighbor not in seen:
                            seen[neighbor]=dist+1
                            q.append((neighbor,dist+1))
        del adj,seen
        answers = []
        def makeSequences(word,seq):
            if word==beginWord:
                answers.append(seq[::-1])
            else:
                for parent in parents[word]:
                    makeSequences(parent,seq+[parent])
        makeSequences(endWord,[endWord])
        return answers
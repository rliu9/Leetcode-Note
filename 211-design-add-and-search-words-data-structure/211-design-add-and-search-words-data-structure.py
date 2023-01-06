class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for s in word:
            if s not in node.children:
                node.children[s] = TrieNode()
            node = node.children[s]
        node.word = True

    def search(self, word: str) -> bool:
        return self.dfs(word, 0, self.root)
        
    def dfs(self, word, idx, root):
        node = root
        for i in range(idx, len(word)):
            if word[i] == '.':
                for child in node.children.values():
                    if self.dfs(word, i+1, child):
                        return True
                return False
            else:
                if word[i] not in node.children:
                    return False
                node = node.children[word[i]]
                return self.dfs(word, i+1, node)
        return node.word


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
        
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for s in word:
            if s not in node.children:
                node.children[s] = TrieNode()
            node = node.children[s]
        node.isWord = True

    def search(self, word: str) -> bool:
        return self.dfs(0, self.root, word)
        
    def dfs(self, idx, root, word):
        node = root
        for i in range(idx, len(word)):
            s = word[i]
            if word[i] == '.':
                for child in node.children.values():
                    if self.dfs(i+1, child, word):
                        return True
                return False
            else:
                if s not in node.children:
                    return False
                node = node.children[s]
        return node.isWord

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
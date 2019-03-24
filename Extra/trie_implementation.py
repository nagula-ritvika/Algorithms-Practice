#__author__ = ritvikareddy2
#__date__ = 2019-03-23

from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_word = False


class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        node = self.root
        for letter in word:
            node = node.children[letter]

        node.is_word = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        for letter in word:
            node = node.children.get(letter)
            if node is None:
                return False
        return node.is_word

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for letter in prefix:
            node = node.children.get(letter)
            if node is None:
                return False
        return True

    def getWordsStartingWith(self, prefix):
        node = self.root
        res = []
        for letter in prefix:
            node = node.children.get(letter)

        self.dfs(node, prefix, res)
        return res

    def dfs(self, node, word, res):
        if node.is_word:
            res.append(word)
            return

        for next_letter in node.children:
            self.dfs(node.children.get(next_letter), word + next_letter, res)

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


if __name__ == '__main__':
    trie = Trie()
    trie.insert('Alan')
    trie.insert('Alex')

    print(trie.getWordsStartingWith('Al'))

    trie.insert('Bob')
class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()        # splits by spaces and removes extra spaces
        words.reverse()          # reverse the list of words
        return " ".join(words)   # join with single space

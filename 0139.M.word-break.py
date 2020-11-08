# 139. 单词拆分
# https://leetcode-cn.com/problems/word-break/

from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)

        def indexWords(idx: int) -> bool:
            if idx == len(s):
                return True
            for i in range(idx + 1, len(s) + 1):
                word = s[idx:i]
                if word in wordSet:
                    if indexWords(i):
                        return True
            return False

        return indexWords(0)


testcase = [
    ("leetcode", ["leet", "code"]),
    ("applepenapple", ["apple", "pen"]),
    ("catsandog", ["cats", "dog", "sand", "and", "cat"]),
    ("aaaaaaa", ["aaaa", "aaa"]),
]

if __name__ == "__main__":
    obj = Solution()
    for s, wordDict in testcase:
        print(obj.wordBreak(s, wordDict))

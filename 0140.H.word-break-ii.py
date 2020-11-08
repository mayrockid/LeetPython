# 140. 单词拆分 II
# https://leetcode-cn.com/problems/word-break-ii/

from typing import List, Set
from functools import lru_cache


# 96ms
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        @lru_cache(None)
        def indexWords(idx: int) -> List[List[str]]:
            if idx == len(s):
                return [[]]
            line_list = []
            for i in range(idx + 1, len(s) + 1):
                word = s[idx:i]
                if word in wordDict:
                    _line_list = indexWords(i)
                    for _line in _line_list:
                        line_list.append(_line + [word])
            return line_list

        lines = indexWords(0)
        return [" ".join(line[::-1]) for line in lines]


# 官方题解 36ms
class Solution2:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        @lru_cache(None)
        def backtrack(index: int) -> List[List[str]]:
            if index == len(s):
                return [[]]
            ans = list()
            for i in range(index + 1, len(s) + 1):
                word = s[index:i]
                if word in wordSet:
                    nextWordBreaks = backtrack(i)
                    for nextWordBreak in nextWordBreaks:
                        ans.append(nextWordBreak.copy() + [word])
            return ans
        
        ################################################################
        wordSet = set(wordDict) # !!! set 比 list 快 !!! #
        ################################################################
        breakList = backtrack(0)
        return [" ".join(words[::-1]) for words in breakList]


# 执行用时为 32 ms 的范例
class Solution3:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        if len(set(s)) > len(set("".join(wordDict))):
            return []
        wordDict = set(wordDict)
        N = len(s)
        dp = [[] for i in range(N)]
        for i in range(N):
            word = s[:i + 1]
            if word in wordDict:
                dp[i].append([i])
        for i in range(N):
            if dp[i]:
                break
        for j in range(i + 1, N):
            for k in range(j):
                if dp[k] and s[k + 1:j + 1] in wordDict:
                    for L in dp[k]:
                        dp[j].append(L[:] + [j])
        L = dp[-1]
        ans = []
        for index in L:
            #print(index)
            wordList = [s[:index[0] + 1]]
            for i in range(len(index) - 1):
                wordList.append(s[index[i] + 1:index[i + 1] + 1])
            ans.append(" ".join(wordList))
        return ans


testcase = [
    ("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
     ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]),
    ("catsanddog", ["cat", "cats", "and", "sand", "dog"]),
    ("pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"]),
    ("catsandog", ["cats", "dog", "sand", "and", "cat"]),
]

if __name__ == "__main__":
    obj = Solution()
    for s, wordDict in testcase:
        print(obj.wordBreak(s, wordDict))
        # break

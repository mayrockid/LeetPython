# 127. 单词接龙
# https://leetcode-cn.com/problems/word-ladder/

from typing import List
import collections


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def addWord(word: str):
            if word not in wordId:
                nonlocal nodeNum
                wordId[word] = nodeNum
                nodeNum += 1

        def addEdge(word: str):
            addWord(word)
            id1 = wordId[word]
            chars = list(word)
            for i in range(len(chars)):
                tmp = chars[i]
                chars[i] = "*"
                newWord = "".join(chars)
                addWord(newWord)
                id2 = wordId[newWord]
                edge[id1].append(id2)
                edge[id2].append(id1)
                chars[i] = tmp

        wordId = dict()
        edge = collections.defaultdict(list)
        nodeNum = 0

        for word in wordList:
            addEdge(word)

        addEdge(beginWord)
        if endWord not in wordId:
            return 0

        dis = [float("inf")] * nodeNum
        beginId, endId = wordId[beginWord], wordId[endWord]
        dis[beginId] = 0

        que = collections.deque([beginId])
        while que:
            x = que.popleft()
            if x == endId:
                return dis[endId] // 2 + 1
            for it in edge[x]:
                if dis[it] == float("inf"):
                    dis[it] = dis[x] + 1
                    que.append(it)

        return 0


# class Solution:
#     def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
#         if endWord not in wordList:
#             return 0

#         from functools import lru_cache

#         @lru_cache
#         def checkWord(word1: str, word2: str) -> bool:
#             if len(word1) != len(word2):
#                 return False
#             else:
#                 cnt = 0
#                 for i in range(len(word1)):
#                     cnt += 1 if word1[i] != word2[i] else 0
#                 return cnt == 1

#         @lru_cache
#         def filterWord(word: str) -> List[str]:
#             l = []
#             for w in wordList:
#                 if checkWord(w, word):
#                     l.append(w)
#             return l

#         from typing import Set

#         res = []
#         res_route = []

#         def findRoute(word: str, route: List[str]):
#             wl = filterWord(word)
#             for w in wl:
#                 if w == endWord:
#                     res.append(len(route) + 1)
#                     res_route.append(route.append(w))
#                 elif w in route:
#                     continue
#                 else:
#                     r = route.copy()
#                     r.append(w)
#                     if res and len(r) >= min(res):
#                         continue
#                     else:
#                         findRoute(w, r)

#         findRoute(beginWord, [beginWord])

#         if res:
#             return min(res)
#         else:
#             return 0

testcase = [
    [ 'hit', 'cog', [ "hot", "dot", "dog", "lot", "log", "cog"], 5 ],
    [ 'hit', 'dot', [ "hot", "dot", "dog", "lot", "log", "cog"], 3 ],
    [ 'hit', 'cog', [ "hot", "dot", "dog", "lot", "log"], 0 ],
    [
        "qa", "sq",
        [
            "si", "go", "se", "cm", "so", "ph", "mt", "db", "mb", "sb", "kr", "ln", "tm", "le", "av", "sm", "ar", "ci", "ca", "br", "ti", "ba", "to", "ra", "fa", "yo", "ow", "sn",
            "ya", "cr", "po", "fe", "ho", "ma", "re", "or", "rn", "au", "ur", "rh", "sr", "tc", "lt", "lo", "as", "fr", "nb", "yb", "if", "pb", "ge", "th", "pm", "rb", "sh", "co",
            "ga", "li", "ha", "hz", "no", "bi", "di", "hi", "qa", "pi", "os", "uh", "wm", "an", "me", "mo", "na", "la", "st", "er", "sc", "ne", "mn", "mi", "am", "ex", "pt", "io",
            "be", "fm", "ta", "tb", "ni", "mr", "pa", "he", "lr", "sq", "ye"
        ], 5
    ],
]

if __name__ == '__main__':
    o = Solution()
    total, cnt = 0, 0
    for beginWord, endWord, wordList, except_ in testcase:
        print(f'beginWord = {beginWord}')
        print(f'endWord = {endWord}')
        print(f'wordList = {wordList}')
        print(f'except_ = {except_}')
        actual = o.ladderLength(beginWord, endWord, wordList)
        print(f'actual = {actual}')
        print(f'result = {actual == except_}\n')
        cnt += 1 if actual == except_ else 0
        total += 1

    print(f'Total = {total}, correct = {cnt}, {cnt/total*100:.2f}%.')
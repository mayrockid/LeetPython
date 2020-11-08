# 3. 无重复字符的最长子串
# https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/


# 40ms
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = ""
        f = ""
        for i in range(len(s)):
            if s[i] not in f:
                f += s[i]
            else:
                if len(d) < len(f):
                    d = f
                f = f[f.index(s[i]) + 1::] + s[i]
        return max(len(d), len(f))


# 3808ms
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        for left in range(len(s)):
            for right in range(left + 1, len(s) + 1):
                if len(set(s[left:right])) < right - left:
                    break
                if right - left > max_length:
                    max_length = right - left

        return max_length


testcase = [
    'au',
    'abcabcbb',
    'bbbbb',
    'pwwkew',
    '',
    ' ',
]

if __name__ == '__main__':
    obj = Solution()
    for s in testcase:
        print(obj.lengthOfLongestSubstring(s))
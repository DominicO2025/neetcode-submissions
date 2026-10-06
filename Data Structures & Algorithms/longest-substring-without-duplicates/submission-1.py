class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub = set()
        longest = 0
        left = 0

        for i in range(len(s)):

            while s[i] in sub:
                sub.remove(s[left])
                left += 1

            sub.add(s[i])

            longest = max(longest, len(sub))

        return longest
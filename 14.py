class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        # Sort the strings to make it easier to find the common prefix
        strs.sort()
        # Consider the first and last strings after sorting
        first_str = strs[0]
        last_str = strs[-1]
        # Find the common prefix between the first and last strings
        common_prefix = []
        for i in range(len(first_str)):
            if i < len(last_str) and first_str[i] == last_str[i]:
                common_prefix.append(first_str[i])
            else:
                break
        return ''.join(common_prefix)
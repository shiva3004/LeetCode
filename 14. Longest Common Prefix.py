class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        j = 0
        if len(strs) == 0:
            return ""
        prefix = strs[0]
        print(len(strs), len(prefix))
        for i in  range(1, len(strs)):
            for j in range(0 , len(prefix)):
                if j < len(strs[i]) and prefix[j] == strs[i][j]:
                    continue
                else:
                    prefix = prefix[:j]
                    break
            prefix = prefix[:j+1]
            print(strs[i],prefix)
            if prefix == "":
                print('empty')
                return prefix
        return prefix

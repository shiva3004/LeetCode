class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hm = collections.defaultdict(list)
        res_set = []
        for i in range(len(strs)):
            s = ''.join(sorted(strs[i]))
            hm[s].append(strs[i])
        return hm.values()
        

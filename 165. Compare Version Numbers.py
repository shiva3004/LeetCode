class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        i = 0; j = 0
        arr_version1 = version1.split('.'); arr_version2 = version2.split('.')
        while i < len(arr_version1) and j < len(arr_version2):
            v1 = int(arr_version1[i]); v2 = int(arr_version2[j])
            if v1 > v2:
                return 1
            elif v1 < v2:
                return -1
            else:
                i += 1
                j += 1
        while i < len(arr_version1) and int(arr_version1[i]) == 0:
            i += 1
        while j < len(arr_version2) and int(arr_version2[j]) == 0:
            j += 1
        
        
        if i < len(arr_version1) and j == len(arr_version2):
            return 1
        elif i == len(arr_version1) and j < len(arr_version2):
            return -1
        elif i == len(arr_version1) and j == len(arr_version2):
            return 0

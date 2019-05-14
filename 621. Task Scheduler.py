class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        arr = [0 for i in range(26)]
        res = 0
        for a in tasks:
            arr[65 - ord(a)] += 1
        arr = sorted(arr)[::-1]
        while arr[0] > 0:
            width = -1
            for i in range(len(arr)):
                if arr[i] == 0 or width == n:
                    break
                res += 1; width += 1
                arr[i] -= 1
            res += (n - width) if arr[0] > 0 else 0
            arr = sorted(arr)[::-1]
        return res

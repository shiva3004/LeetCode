class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        queue = [(start, 0)]
        bank_set = set(bank)
        
        while queue:
            str, step = queue.pop(0)
            if str == end:
                return step
            for i in range(len(str)):
                for c in 'ACGT':
                    mutate = str[:i] + c + str[i+1:]
                    if mutate in bank_set:
                        bank_set.remove(mutate)
                        queue.append((mutate, step + 1))
        return -1

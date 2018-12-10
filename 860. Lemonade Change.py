class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        mapper = { 5 : 0, 10 : 0, 20 : 0 }
        for bill in bills:
            mapper[bill] += 1
            if bill == 10:
                if mapper[5] == 0:
                    return False
                mapper[5] -= 1
            elif bill == 20:
                if mapper[10] == 0 and mapper[5] == 0:
                    return False
                elif mapper[5] == 0:
                    return False
                elif mapper[10] == 0:
                    if mapper[5] < 3:
                        return False
                    mapper[5] -= 3
                else:
                    mapper[10] -= 1
                    mapper[5] -= 1
        return True
                      

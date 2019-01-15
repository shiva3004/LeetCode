class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        mapper = collections.defaultdict(list)
        for pre in prerequisites:
            mapper[pre[0]].append(pre[1])
        #print(mapper)
        visited = {}
        for pre in prerequisites:
            i = pre[0]
            seen = set()
            if not self.canbeValidCourse(i, mapper, seen, visited):
                return False
        return True
    
    def canbeValidCourse(self, i, mapper, seen, visited):
        #print(i, mapper, seen)
        if i in visited:
            return visited[i]
        if i in seen:
            return False
        if i not in mapper.keys():
            return True
        for c in mapper[i]:
            seen.add(i)
            if not self.canbeValidCourse(c, mapper, seen, visited):
                visited[c] = False
                visited[i] = False
                return False
            else:
                visited[c] = True
            seen.remove(i)
        visited[i] = True
        return True

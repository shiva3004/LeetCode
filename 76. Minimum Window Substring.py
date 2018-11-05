class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        mapper_t = collections.Counter(t)
        l = r = 0
        window_map = {}
        formed = 0
        ans = [float('inf'), -1, -1]
        
        required = len(mapper_t)
        while r < len(s):
            c = s[r]
            
            if c not in window_map:
                window_map[c] = 0
            window_map[c] += 1
            
            if window_map[c] == mapper_t[c]:
                formed += 1
            
            while l <= r and formed == required:
                c = s[l]
                if r - l + 1 < ans[0]:
                    ans[0] = r - l + 1
                    ans[1] = l; ans[2] = r + 1
                window_map[c] -= 1
                if c in mapper_t and window_map[c] < mapper_t[c]:
                    formed -= 1
                l += 1
            r += 1
        
        return s[ans[1] : ans[2]]
                
                
                

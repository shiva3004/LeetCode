class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        c = m+n-1
        m -= 1
        n -= 1
        while n >= 0:
            print(m ,n)
            if m >=0 and nums1[m] > nums2[n]:
                nums1[c] = nums1[m]
                m -= 1
            else:
                nums1[c] = nums2[n]
                n -= 1
            c -= 1

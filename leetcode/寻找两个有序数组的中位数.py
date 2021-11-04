class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        n = len(nums1) + len(nums2)
        if n % 2 == 1:
            return self.findKth(nums1, nums2, n//2)
        else:
            return (self.findKth(nums1, nums2, n//2) + self.findKth(nums1, nums2, n//2 - 1))/2

    def findKth(self, nums1, nums2, k):
        if not nums1:
            return nums2[k]
        if not nums2:
            return nums1[k]
        i1, i2 = len(nums1) // 2, len(nums2) // 2
        #print(i1, i2)
        m1, m2 = nums1[i1], nums2[i2]

        if i1 + i2 < k:
            if m1 > m2:
                self.findKth(nums1, nums2[i2 + 1], k - i2 - 1)
            else:
                self.findKth(nums1[i1 + 1:], nums2, k - i1 - 1)
        else:
            if m1 > m2:
                self.findKth(nums1[:i1], nums2, k)
            else:
                self.findKth(nums1, nums2[:i2], k)
        return m2
if __name__ =='__main__':
    nums1 = [1,2,3]
    nums2 = [4,5]
    solution =Solution()
    print(solution.findMedianSortedArrays(nums1,nums2))
lass Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        checker1 = set(nums1)
        checker2 = set(nums2)

        result =[]
        check1 = []
        check2 = []

        for i in checker1:
            if i not in checker2:
                check1.append(i)

        result.append(check1)

        for i in checker2:
            if i not in checker1:
                check2.append(i)
        result.append(check2)
        return result

        



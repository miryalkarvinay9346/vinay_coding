class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        result = []
        for num in arr2:
            count = arr1.count(num)
            result.extend([num] * count)
        remaining = sorted([num for num in arr1 if num not in arr2])
        result.extend(remaining)
        return result
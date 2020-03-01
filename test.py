class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits_str = ''
        for i in range(len(digits)):
            digits_str += str(digits[i])
        digits_num = int(digits_str) + 1
        digits_list = list(str(digits_num))
        return digits_list


a = Solution()
print(a.plusOne([1, 2, 3]))
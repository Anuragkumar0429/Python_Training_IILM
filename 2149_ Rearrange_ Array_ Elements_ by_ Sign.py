class Solution:
    def rearrangeArray(self, nums):
        pos = []
        neg = []

        # Step 1: separate positives and negatives
        for num in nums:
            if num > 0:
                pos.append(num)
            else:
                neg.append(num)

        # Step 2: merge alternately
        result = []
        for i in range(len(pos)):
            result.append(pos[i])
            result.append(neg[i])

        return result

class Solution(object):
    def countBits(self, num):
        """
        :type n: int
        :rtype: List[int]
        """
        counter = [0]
        for i in range(1, num+1):
            counter.append(counter[i >> 1] + i % 2)
        return counter
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
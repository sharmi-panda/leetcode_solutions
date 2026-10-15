class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        length = 1
        count = 9
        start = 1

        while n > length * count:
            n -= length * count
            length += 1
            count *= 10
            start *= 10

        number = start + (n - 1) // length
        digit_index = (n - 1) % length

        return int(str(number)[digit_index])


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
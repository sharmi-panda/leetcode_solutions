class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        
        if num == 0:
            return "Zero"

        below_20 = [
            "", "One", "Two", "Three", "Four", "Five", "Six",
            "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve",
            "Thirteen", "Fourteen", "Fifteen", "Sixteen",
            "Seventeen", "Eighteen", "Nineteen"
        ]

        tens = [
            "", "", "Twenty", "Thirty", "Forty", "Fifty",
            "Sixty", "Seventy", "Eighty", "Ninety"
        ]

        thousands = ["", "Thousand", "Million", "Billion"]

        def helper(n):
            if n == 0:
                return ""

            if n < 20:
                return below_20[n]

            if n < 100:
                rest = helper(n % 10)

                if rest:
                    return tens[n // 10] + " " + rest

                return tens[n // 10]

            rest = helper(n % 100)

            if rest:
                return below_20[n // 100] + " Hundred " + rest

            return below_20[n // 100] + " Hundred"

        words = []
        i = 0

        while num > 0:
            chunk = num % 1000

            if chunk != 0:
                part = helper(chunk)

                if thousands[i]:
                    part = part + " " + thousands[i]

                words.append(part)

            num //= 1000
            i += 1

        return " ".join(reversed(words))

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
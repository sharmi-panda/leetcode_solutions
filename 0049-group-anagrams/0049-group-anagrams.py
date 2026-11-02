class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagram_map ={}
        
        for word in strs:
            count = [0] *26
            for char in word:
                count[ord(char)- 97]+= 1

            key = tuple(count)
            anagram_map.setdefault(key,[]).append(word)
        return anagram_map.values()

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
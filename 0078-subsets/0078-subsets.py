class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result=[]
        path=[]

        def dfs(start):
            result.append(path[:])

            for i in range(start,len(nums)):
                path.append(nums[i])
                dfs(i+1)
                path.pop()

        dfs(0)
        return result

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
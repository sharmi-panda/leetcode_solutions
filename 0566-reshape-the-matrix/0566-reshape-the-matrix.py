class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if len(mat) * len(mat[0]) != r * c:
            return mat
        flat_list = []
        for row in mat:
            for num in row:
                flat_list.append(num)
                reshaped = []
        for i in range(0, len(flat_list), c):
            reshaped.append(flat_list[i : i + c])
            
        return reshaped
      
      
      
      

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
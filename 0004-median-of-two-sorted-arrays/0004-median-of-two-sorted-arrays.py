class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        lista = (nums1+nums2)
        lista.sort()
        tamanho_lista = len(lista)
        if tamanho_lista%2 == 0:
            return sum(lista[(tamanho_lista//2)-1:(tamanho_lista//2)+1:])/2.0
        else:
            return lista[tamanho_lista//2]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
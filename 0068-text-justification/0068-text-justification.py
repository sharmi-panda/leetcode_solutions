class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        res,cur,num_of_letters=[],[],0

        for w in words:
            if num_of_letters+len(w)+len(cur)>maxWidth:
                for i in range(maxWidth-num_of_letters):
                    cur[i%(len(cur)-1 or 1)]+=" "
                res.append("".join(cur))
                cur,num_of_letters=[],0
            cur.append(w)
            num_of_letters+=len(w)
        last_line=" ".join(cur)
        last_line+=" "*(maxWidth-len(last_line))

        return res+[last_line]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
class Solution(object):
    def validTicTacToe(self, board):
        """
        :type board: List[str]
        :rtype: bool
        """
        x = sum(row.count("X") for row in board)
        o = sum(row.count("O") for row in board)

        if x < o or x > o + 1:
            return False

        def win(c):
            for i in range(3):
                if board[i][0] == board[i][1] == board[i][2] == c:
                    return True
                if board[0][i] == board[1][i] == board[2][i] == c:
                    return True

            if board[0][0] == board[1][1] == board[2][2] == c:
                return True

            if board[0][2] == board[1][1] == board[2][0] == c:
                return True

            return False

        if win("X") and x == o:
            return False

        if win("O") and x > o:
            return False

        if win("X") and win("O"):
            return False

        return True

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
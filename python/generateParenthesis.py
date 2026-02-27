class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []

        def backtrack(s, abiertos, cerrados):
            if len(s) == 2 * n:
                res.append(s)
                return

            if abiertos < n:
                backtrack(s + "(", abiertos + 1, cerrados)

            if cerrados < abiertos:
                backtrack(s + ")", abiertos, cerrados + 1)

        backtrack("", 0, 0)
        return res
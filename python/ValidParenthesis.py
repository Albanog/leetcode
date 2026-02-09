class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        '(', ')', '{', '}', '[',']'
        """
        cant_chars = len(s)
        i=0
        stack = []
        for char in s:
            i+=1
            if char == '(' or char == '[' or char == '{' :
                stack.append(char)
            else:
                if stack:
                    aux = stack.pop()
                    if ( char == ')' and aux != '(' ) or ( char == ']' and aux != '[' ) or ( char == '}' and aux != '{' ):
                        return False
                else:
                    return False  

            if len(stack) > cant_chars -i:
                return False

        if stack:
            return False
        return True
        
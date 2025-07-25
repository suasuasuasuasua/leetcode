# https://leetcode.com/problems/valid-palindrome/description/
class Solution:
    def isValid(self, s: str) -> bool:
        # the problem is to verify that all the paranthesis in the string are
        # balanced correctly
        # valid sets are '()', '{}', and '[]'
        #
        # these are the rules
        # 1. Open brackets must be closed by the same type of brackets.
        # 2. Open brackets must be closed in the correct order.
        # 3. Every close bracket has a corresponding open bracket of the same
        #    type.
        #
        # a stack is a pretty natural solution for this problem. as we add a new
        # character onto the stack, we can check if the last character added
        # is the corresponding character

        # use a list to simulate the stack
        # we can append() and pop() to add and remove to and from the stack
        stack = list()

        mapping = {
            ")": "(",
            "}": "{",
            "]": "[",
        }

        # loop over each of the characters
        for c in s:
            match c:
                # add the opening parenthesis
                case "(" | "{" | "[":
                    stack.append(c)
                # check the closing parenthesis
                case ")" | "}" | "]" if stack and stack[-1] == mapping[c]:
                    stack.pop()
                # otherwise, we must have missed the match
                case _:
                    return False

        # the stack should be empty!
        return not stack

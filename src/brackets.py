# Задача про скобки:
# Given a string is containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
#
# Example 1:
#
# Input: s = "()"
# Output: true
#
# Example 2:
#
# Input: s = "()[]{}"
# Output: true
#
# Example 3:
#
# Input: s = "(]"
# Output: false
#
# № 20 на литкоде


def find_same_brackets(brackets_str: str) -> bool:
    if brackets_str[0] == ")" or brackets_str[0] == "]" or brackets_str[0] == "}":
        return False
    else:
        list_tmp = []
        for char in brackets_str:
            if char == "(" or char == "[" or char == "{":
                list_tmp.append(char)
            else:
                if char == ")":
                    if "(" in list_tmp:
                        list_tmp.remove("(")
                elif char == "]":
                    if "[" in list_tmp:
                        list_tmp.remove("[")
                elif char == "}":
                    if "{" in list_tmp:
                        list_tmp.remove("{")
        if not list_tmp:
            return True
        else:
            return False


print(find_same_brackets("()[]{}"))

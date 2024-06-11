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


def find_same_brackets(s: str) -> bool:
    list_tmp = []
    dict_tmp = {
        "(": ")",
        "[": "]",
        "{": "}"
    }

    for i in s:
        if i in dict_tmp:
            list_tmp.append(i)
        else:
            if not list_tmp or i != dict_tmp[list_tmp.pop()]:
                return False
    return list_tmp == []


print(find_same_brackets("()[]{}"))

import re;
def is_palindrome(input: str):
    sanitized_input = ''.join(re.findall(r'[a-z]+', input.lower()))
    reversed_string = sanitized_input[::-1]
    return sanitized_input == reversed_string

print(is_palindrome("race car"))

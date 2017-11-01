# coding: utf-8


def is_palindrome(s):
    "Checks wether a given string <s> is a palindrome and returns True/False"
    if len(s) <= 1:    # Empty string or single char
        return True

    if s[0] != s[-1]:  # First char should equal last char
        return False

    # Now, we know the first and last are equal,
    # Lets remove those and check again for that
    # Substring until we reach the end.
    return is_palindrome(s[1:-1])


if __name__ == '__main__':
    print("abba", is_palindrome("abba"))
    print("abbas", is_palindrome("abbas"))
    print("5102015", is_palindrome("5102015"))
    print("15.10.15", is_palindrome("15.10.15"))
    print("a", is_palindrome("a"))

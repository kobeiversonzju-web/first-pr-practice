def is_palindrome(s):
    """Return True if s reads the same forwards and backwards, ignoring case and spaces."""
    cleaned = s.lower().replace(" ", "")
    return cleaned == cleaned[::-1]


def reverse_words(s):
    """Return s with the order of its words reversed."""
    return " ".join(s.split()[::-1])

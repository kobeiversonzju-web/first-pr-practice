# first-pr-practice

A tiny Python string-utility library, used as a sandbox for practicing GitHub pull requests.

## Functions

- `is_palindrome(s)` — returns `True` if `s` reads the same forwards and backwards (case- and space-insensitive).
- `reverse_words(s)` — returns `s` with the order of its words reversed.

## Usage

```python
from stringutils import is_palindrome, reverse_words

is_palindrome("Was it a car or a cat I saw")  # True
reverse_words("hello world")                  # "world hello"
```

## Tests

Run the test suite with:

```bash
python -m unittest discover
```

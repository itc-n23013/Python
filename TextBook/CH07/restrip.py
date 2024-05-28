def custom_strip(input_str, chars=None):
    return input_str.strip(chars)

test_str = "   Hello, World!   "
print(custom_strip(test_str))

test_str_with_chars = "***Hello, World!***"
print(custom_strip(test_str_with_chars, "*"))


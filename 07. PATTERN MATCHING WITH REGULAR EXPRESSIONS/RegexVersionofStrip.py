import re

def custom_strip(s, chars=None):
    # If chars is not specified, remove whitespace from the beginning and end
    if chars is None:
        return s.strip()

    # Build a pattern to match characters specified in chars
    pattern = f'^[{re.escape(chars)}]+|[{re.escape(chars)}]+$'
    return re.sub(pattern, '', s)

# Test the function
original_string = "   Hello, World!   "
custom_chars = ",! "

result_default = custom_strip(original_string)
result_custom = custom_strip(original_string, chars=custom_chars)

print(f'Original String: "{original_string}"')
print(f'Result (Default): "{result_default}"')
print(f'Result (Custom): "{result_custom}"')

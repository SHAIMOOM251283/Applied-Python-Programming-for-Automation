def format_list(items):
    if len(items) == 0:
        return ''  # Return an empty string for an empty list
    elif len(items) == 1:
        return str(items[0])  # Return the single item as a string
    else:
        # Use ', '.join() to concatenate all items with commas and spaces
        # Insert 'and' before the last item
        return ', '.join(map(str, items[:-1])) + ', and ' + str(items[-1])

# Get user input for the list
user_input = input("Enter items separated by spaces: ")
user_list = user_input.split()  # Split the input string into a list

# Example usage with user-input list
formatted_string = format_list(user_list)
print(formatted_string)

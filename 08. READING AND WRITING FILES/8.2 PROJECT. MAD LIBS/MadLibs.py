import re

def mad_libs_generator(template_file, output_file):
    # Read the template file
    with open(template_file, 'r') as file:
        template = file.read()

    # Find all placeholders (ADJECTIVE, NOUN, ADVERB, VERB)
    placeholders = re.findall(r'\b(ADJECTIVE|NOUN|ADVERB|VERB)\b', template)

    # Replace each placeholder with user input
    for placeholder in placeholders:
        user_input = input(f"Enter a {placeholder.lower()}: ")
        template = template.replace(placeholder, user_input, 1)

    # Write the modified text to the output file
    with open(output_file, 'w') as file:
        file.write(template)

if __name__ == "__main__":
    template_file_path = "mad_libs_template.txt"
    output_file_path = "mad_libs_output.txt"

    mad_libs_generator(template_file_path, output_file_path)

    print(f"\nMad Libs completed! Check the '{output_file_path}' file.")

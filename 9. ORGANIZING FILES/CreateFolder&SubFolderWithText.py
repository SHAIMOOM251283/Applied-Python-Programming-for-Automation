import os

def create_directory_structure():
    # Specify the main directory path
    main_directory = "my_main_directory"

    # Create the main directory
    os.makedirs(main_directory, exist_ok=True)

    # Create a text file in the main directory
    with open(os.path.join(main_directory, "main_text_file.txt"), "w") as main_file:
        main_file.write("This is the main text file.")

    # Create a sub-directory
    sub_directory = os.path.join(main_directory, "my_sub_directory")
    os.makedirs(sub_directory, exist_ok=True)

    # Create a text file in the sub-directory
    with open(os.path.join(sub_directory, "sub_text_file.txt"), "w") as sub_file:
        sub_file.write("This is the sub-text file.")

if __name__ == "__main__":
    create_directory_structure()

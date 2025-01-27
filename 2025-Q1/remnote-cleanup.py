
import os

def remove_string_from_markdown_files(directory, target_string):
    """
    Recursively traverse the directory, open Markdown files, and remove the target string from them.

    Args:
        directory (str): The directory to start the search.
        target_string (str): The string to be removed from Markdown files.
    """
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".md"):  # Check if the file is a Markdown file
                file_path = os.path.join(root, file)
                try:
                    # Open the file, read content, remove the target string, and write back
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()

                    updated_content = content.replace(target_string, "")

                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(updated_content)

                    print(f"Processed: {file_path}")
                except Exception as e:
                    print(f"Error processing {file_path}: {e}")

if __name__ == "__main__":
    current_directory = os.getcwd()  # Get the current working directory
    string_to_remove = ">>>"         # The string to remove
    remove_string_from_markdown_files(current_directory, string_to_remove)

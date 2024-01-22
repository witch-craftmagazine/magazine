import os
import re

def process_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    # Use regex to find and replace the string between png and Alt
    content = re.sub(r'(png)(Alt)', r'\1\n\2', content)

    with open(file_path, 'w') as file:
        file.write(content)

def process_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.ini'):
                file_path = os.path.join(root, file)
                process_file(file_path)
                print(f"Processed: {file_path}")

# Replace 'your_directory_path' with the path to the directory containing your .ini files
directory_path = 'comics'
process_directory(directory_path)
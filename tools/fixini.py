import os
import re

def process_ini_file(file_path):
    modified_lines = []
    modified = False

    with open(file_path, 'r') as f:
        for line in f:
            # Check if the line contains 'Filename'
            if 'Filename' in line:
                # Replace 'Filename = Filename = ' with 'Filename = '
                line = re.sub(r'^\s*Filename\s*=\s*Filename\s*=\s*', 'Filename = ', line)
                # Replace .png with .jpg
                line = line.replace('.png', '.jpg')
                modified = True
            modified_lines.append(line)

    # Write modified content back to the file
    if modified:
        with open(file_path, 'w') as f:
            f.writelines(modified_lines)
            print(f"Modified: {file_path}")

def process_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file_name in files:
            if file_name.endswith('.ini'):
                file_path = os.path.join(root, file_name)
                process_ini_file(file_path)

# Start processing from the current directory
process_directory('.')

import os
import shutil

def create_directory_structure(root_directory):
    # Find all PNG files recursively and iterate over them
    for root, dirs, files in os.walk(root_directory):
        for file in files:
            if file.lower().endswith(".png"):
                # Create a new directory for each PNG file
                new_directory = os.path.join(root, os.path.splitext(file)[0])
                os.makedirs(new_directory, exist_ok=True)

                # Move the PNG file into the new directory
                source_path = os.path.join(root, file)
                destination_path = os.path.join(new_directory, file)
                shutil.move(source_path, destination_path)

                # Create info.ini and post.txt files
                info_file_path = os.path.join(new_directory, "info.ini")
                post_file_path = os.path.join(new_directory, "post.txt")
                open(info_file_path, 'a').close()
                open(post_file_path, 'a').close()

                # Extract relevant information
                title = os.path.basename(file)
                post_date = "June 3, 2024"
                filename = os.path.basename(file)
                alt_text = "I will write it out I promise..."
                storyline = os.path.basename(os.path.dirname(new_directory))
                characters = ""
                tags = ""

                # Write to info.ini
                with open(info_file_path, 'w') as info_file:
                    info_file.write(f"Title = {title}\n")
                    info_file.write(f"Post date = {post_date}\n")
                    info_file.write(f"Filename = {filename}\n")
                    info_file.write(f"Alt text = {alt_text}\n")
                    info_file.write(f"Storyline = {storyline}\n")
                    info_file.write(f"Characters = {characters}\n")
                    info_file.write(f"Tags = {tags}\n")

# Replace "/path/to/your/root/directory" with the actual path to your root directory
root_directory = "issue15"
create_directory_structure(root_directory)

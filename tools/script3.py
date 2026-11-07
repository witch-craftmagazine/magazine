import os
import shutil
from datetime import datetime

def create_folder_structure(source_folder):
    # List all image files in the source folder
    image_files = [f for f in os.listdir(source_folder) if f.lower().endswith(('.png'))]

    # Create a unique folder for each image file
    for image_file in image_files:
        # Extract file name without extension
        file_name = os.path.splitext(image_file)[0]
        
        # Create a unique folder path based on the file name
        folder_path = os.path.join(source_folder, file_name)
        
        # Create the folder if it doesn't exist
        os.makedirs(folder_path, exist_ok=True)
        
        # Move the image file to the corresponding folder
        shutil.move(os.path.join(source_folder, image_file), os.path.join(folder_path, image_file))
        
        # Create and copy info.ini to the folder
        with open(os.path.join(folder_path, 'info.ini'), 'w') as info_file:
            # Populate info.ini with title, post date, and filename
            info_file.write(f"Title = {file_name}\n")
            info_file.write(f"Post date = {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            info_file.write(f"Filename = {image_file}")
            info_file.write("Alt text = I will write it out I promise...\n")
            info_file.write("Storyline = issue 13\n")
            info_file.write("Characters = \n")
            info_file.write("Tags = ")

        # Create and copy post.txt to the folder
        with open(os.path.join(folder_path, 'post.txt'), 'w') as post_file:
            post_file.write("This is the post.txt file for {}".format(file_name))

if __name__ == "__main__":
    # Replace 'your_source_folder' with the path to your source folder containing image files
    create_folder_structure('issue13')

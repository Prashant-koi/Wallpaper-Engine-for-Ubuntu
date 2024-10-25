import subprocess
import os
import random
import schedule
import time

# Path to the directory with images
path = "your/file/path"

def set_wallpaper():
# Ensure the directory exists
    if not os.path.exists(path):
        print("Directory does not exist.")
        exit(1)

    # Get all files in the directory
    files = os.listdir(path)

    # Filter to include only image files
    image_files = [f for f in files if f.endswith(('.png', '.jpg', '.gif', '.jpeg'))]

    # Check if any image files were found
    if image_files:
        # Select a random image
        random_image = random.choice(image_files)
        
        # Build the full file path
        new_path_one = os.path.join(path, random_image)
        

        # Convert to a file URI (required by gsettings)
        new_path = "file://" + os.path.abspath(new_path_one)

        gsettings_command = f'gsettings set org.gnome.desktop.background picture-uri "{new_path}"'
        subprocess.run(gsettings_command, shell=True)
        

        print(f"Wallpaper set to: {new_path}")
    else:
        print("No image files found.")


schedule.every(1).minutes.do(set_wallpaper)

set_wallpaper()

while True:
    schedule.run_pending()
    time.sleep(1)







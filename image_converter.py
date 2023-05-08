import os
from PIL import Image

def convert_folder_to_webp(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                # Only convert image files with extensions .png, .jpg, or .jpeg
                image_path = os.path.join(root, file)
                output_folder = os.path.join(root, 'webp')
                if not os.path.exists(output_folder):
                    os.makedirs(output_folder)
                output_path = os.path.join(output_folder, os.path.splitext(file)[0] + '.webp')
                im = Image.open(image_path)
                im.save(output_path, 'webp')

# Example usage
convert_folder_to_webp('/path/to/folder')

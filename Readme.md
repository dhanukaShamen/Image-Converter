# Image Converter
This Python program converts PNG, JPG, and JPEG format images to WEBP format. It can convert all images in a specified folder and its subfolders, and save the converted images to a new subfolder within the same folder as the original images.

*Created by Dhanuka Shamen with assistance from ChatGPT.*

## Installation
1. Install Python 3.x if it is not already installed on your computer.
2. Install the Pillow library by running `pip install Pillow` in a command prompt or terminal.

## Usage
1.Import the convert_folder_to_webp function from the image_converter module:

```python
from image_converter import convert_folder_to_webp
```
2.Call the convert_folder_to_webp function with the path to the folder containing the images you want to convert:

```python
convert_folder_to_webp('/path/to/folder')
```
3.The program will convert all images in the specified folder and its subfolders, and save the converted images to a new subfolder called webp within the same folder as the original images.

## Examples
### Convert all images in a folder and its subfolders
 
```python
from image_converter import convert_folder_to_webp

convert_folder_to_webp('/path/to/folder')
```

This will convert all images in the folder **'/path/to/folder'** and its subfolders, and save the converted images to a new subfolder called **'webp'** within the same folder as the original images.

## License
This program is licensed under the MIT License. See the LICENSE file for more information.

**© 2023 ChatGPT and Dhanuka Shamen. All Rights Reserved.**
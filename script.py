"""
The purpose of this program is to generate a PD and save it locally.
"""
from PIL import Image, ImageDraw, ImageFont
import time
import os
import logging

DUCK_COLOR = 'hotpink'
CREATE_INTERVAL = 60 # Seconds

def generate_image():
    """
    Generates an image of a duck.

    Parameters:
    None.

    Returns:
    PIL.Image.Image: An image object of the generated duck.
    """
    # Create an image with light blue background
    img = Image.new('RGB', (200, 200), color='lightblue')
    draw = ImageDraw.Draw(img)

    # Draw the body
    draw.ellipse((50, 70, 150, 170), fill=DUCK_COLOR, outline='black')

    # Draw the head
    draw.ellipse((70, 30, 130, 90), fill=DUCK_COLOR, outline='black')

    # Draw the beak
    draw.polygon([(100, 60), (140, 70), (140, 80), (100, 80)], fill='orange', outline='black')
    draw.polygon([(100, 70), (140, 80), (140, 90), (100, 90)], fill='orange', outline='black')

    # Draw the eye
    draw.ellipse((90, 50, 110, 70), fill='white', outline='black')
    draw.ellipse((95, 55, 105, 65), fill='black')

    # Add the text
    text = 'PD'
    font = ImageFont.load_default()
    text_x = 10
    text_y = img.height - 20
    draw.text((text_x, text_y), text, font=font, fill="black")

    return img

def save_image(image, directory, filename):
    """
    Saves the specified image to the specified file path.
    
    Parameters:
    image (Pillow.Image.Image): The image to save to as a file.
    directory (str): The path to the file location.
    filename (str): The file name.

    Returns:
    None.
    """
    if not os.path.exists(directory):
        os.makedirs(directory)
    image_path = os.path.join(directory, filename)
    image.save(image_path, 'PNG')
    print(f"Image saved locally at {image_path}")

# Main execution logic
if __name__ == '__main__':
    while True:
        datestamp = time.strftime('%Y-%m-%d')
        timestamp = time.strftime('%H-%M')
        directory = f'/ducks/{datestamp}'
        filename = f'{timestamp}.png'
        image = generate_image()
        save_image(image, directory, filename)
        logging.info(f'Saved duck at {datestamp}/{timestamp}')
        time.sleep(CREATE_INTERVAL)

# For viewing the generated image without saving it.
# if __name__ == '__main__':
#     image = generate_image()
#     image.show()

from PIL import Image, ImageDraw
import os

RADIUS = 70

INPUT_DIR = 'input_images'
OUTPUT_DIR = 'output_images'

def round_edges(input_path, output_path):

    image = Image.open(input_path)

    # A luminance mask uses black and white pixel to specify where an image should be transparent. 
    # Black means transparent, white non-transparent.
    # The zero parameter starts the mask as all black.
    mask = Image.new("L", image.size, 0)

    draw = ImageDraw.Draw(mask)

    # Draws a white rectangle with rounded edges on the mask
    draw.rounded_rectangle((0,0) + image.size, RADIUS, fill=255)

    result = image.copy()
    # Applies the mask to the image
    result.putalpha(mask)

    result.save(output_path)


def process_folder():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
    
    for filename in os.listdir(INPUT_DIR):
        if filename.lower().endswith(('.png','.jpg','.jpeg')):
            input_path = os.path.join(INPUT_DIR, filename)
            output_path = os.path.join(OUTPUT_DIR, os.path.splitext(filename)[0] + '_rounded' + '.png')
            print(f"About to process file: {filename}")
            round_edges(input_path, output_path)
            print(f"Finished processing file: {filename}")
        else:
            print(f"Skipping non-image file: {filename}")


process_folder()
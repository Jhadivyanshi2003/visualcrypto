from PIL import Image
import random

import matplotlib.pyplot as plt

def generate_shares(image_path, output_path_share1, output_path_share2):
    # Load the image
    image = Image.open(image_path).convert('1')  # Convert image to black and white
    width, height = image.size

    # Create two blank shares
    share1 = Image.new('1', (width * 2, height * 2), 1)  # White background
    share2 = Image.new('1', (width * 2, height * 2), 1)  # White background

    # Access pixel data
    pixels = image.load()
    pixels_share1 = share1.load()
    pixels_share2 = share2.load()

    # Generate shares
    for y in range(height):
        for x in range(width):
            pixel = pixels[x, y]
            # For black pixel, generate complementary patterns
            if pixel == 0:
                pattern = random.choice([
                    ((0, 1), (1, 0)),
                    ((1, 0), (0, 1))
                ])
            else:  # For white pixel, generate identical patterns
                pattern = random.choice([
                    ((0, 0), (1, 1)),
                    ((1, 1), (0, 0))
                ])
            
            # Assign patterns to shares
            for dy in range(2):
                for dx in range(2):
                    pixels_share1[2 * x + dx, 2 * y + dy] = pattern[dy][dx]
                    pixels_share2[2 * x + dx, 2 * y + dy] = 1 - pattern[dy][dx]

    # Save the shares
    share1.save(output_path_share1)
    share2.save(output_path_share2)

def combine_shares(share1_path, share2_path, output_path_combined):
    # Load shares
    share1 = Image.open(share1_path)
    share2 = Image.open(share2_path)

    # Ensure dimensions match
    assert share1.size == share2.size, "Shares must have the same dimensions"

    # Create a blank image for the combined result
    combined = Image.new('1', share1.size, 1)  # White background

    # Access pixel data
    pixels_share1 = share1.load()
    pixels_share2 = share2.load()
    pixels_combined = combined.load()

    # Combine shares
    width, height = share1.size
    for y in range(height):
        for x in range(width):
            pixels_combined[x, y] = pixels_share1[x, y] & pixels_share2[x, y]

    # Save the combined result
    combined.save(output_path_combined)

# Example usage
generate_shares("C:\\Users\\Divyanshi Jha\\Downloads\\input_image.png", "C:\\Users\\Divyanshi Jha\\Downloads\\share1.png", "C:\\Users\\Divyanshi Jha\\Downloads\\share2.png")

combine_shares("share1.png", "share2.png", "combined_output.png")
print("done")

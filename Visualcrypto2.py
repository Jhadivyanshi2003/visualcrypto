from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def combine_shares(share1_path, share2_path, output_combined_path):
    # Load the two share images
    share1 = Image.open(share1_path).convert('1')  # Convert to binary (black-and-white)
    share2 = Image.open(share2_path).convert('1')

    # Convert shares to numpy arrays
    share1_array = np.array(share1)
    share2_array = np.array(share2)

    # Combine the shares using logical OR operation
    combined_array = np.logical_or(share1_array == 0, share2_array == 0)  # Black = 0, White = 255

    # Convert the result back to an image
    combined_image = Image.fromarray((~combined_array).astype(np.uint8) * 255)  # Invert the image

    # Save the combined image
    combined_image.save(output_combined_path)

    # Display the combined image
    plt.figure(figsize=(5, 5))
    plt.title('Combined Shares (Revealed Image)')
    plt.imshow(combined_image, cmap='gray')
    plt.axis('off')
    plt.show()

# Paths to the two shares and output
share1_path = 'share1.png'
share2_path = 'share2.png'
output_combined_path = 'combined.png'

# Combine the shares
combine_shares(share1_path, share2_path, output_combined_path)

from PIL import Image
import numpy as np

def encrypt_image(image_path, key, output_path):
    # Open the image
    img = Image.open(image_path)
    img = img.convert('RGB')  # Ensure image is in RGB format
    pixels = np.array(img)

    # Encrypting the image by adding the key to each pixel value
    encrypted_pixels = (pixels + key) % 100

    # Convert the encrypted pixels back to an image
    encrypted_img = Image.fromarray(encrypted_pixels.astype('uint8'), 'RGB')
    encrypted_img.save(output_path)

def decrypt_image(encrypted_path, key, output_path):
    # Open the encrypted image
    img = Image.open(encrypted_path)
    img = img.convert('RGB')  # Ensure image is in RGB format
    pixels = np.array(img)

    # Decrypting the image by subtracting the key from each pixel value
    decrypted_pixels = (pixels - key) % 100

    # Convert the decrypted pixels back to an image
    decrypted_img = Image.fromarray(decrypted_pixels.astype('uint8'), 'RGB')
    decrypted_img.save(output_path)

# Example usage
encrypt_image('input_image.jpg', 50, 'encrypted_image.jpg')
decrypt_image('encrypted_image.jpg', 50, 'decrypted_image.jpg')

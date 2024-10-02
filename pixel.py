from PIL import Image

def encrypt_image(image_path, key, output_path):
    # Open an image file
    with Image.open(image_path) as img:
        # Load the pixel data
        pixels = img.load()

        # Iterate through each pixel and apply encryption (add key to each pixel)
        for i in range(img.width):
            for j in range(img.height):
                r, g, b = pixels[i, j]
                
                # Encrypt each channel (R, G, B)
                r = (r + key) % 256
                g = (g + key) % 256
                b = (b + key) % 256
                
                # Update pixel value
                pixels[i, j] = (r, g, b)

        # Save the encrypted image
        img.save(output_path)
        print(f"Encrypted image saved as {output_path}")


def decrypt_image(image_path, key, output_path):
    # Open an encrypted image file
    with Image.open(image_path) as img:
        # Load the pixel data
        pixels = img.load()

        # Iterate through each pixel and apply decryption (subtract key from each pixel)
        for i in range(img.width):
            for j in range(img.height):
                r, g, b = pixels[i, j]
                
                # Decrypt each channel (R, G, B)
                r = (r - key) % 256
                g = (g - key) % 256
                b = (b - key) % 256
                
                # Update pixel value
                pixels[i, j] = (r, g, b)

        # Save the decrypted image
        img.save(output_path)
        print(f"Decrypted image saved as {output_path}")


def main():
    while True:
        print("\nSelect an option:")
        print("1: Encrypt an image")
        print("2: Decrypt an image")
        print("0: Exit")
        
        choice = input("Enter your choice (1/2/0): ")

        if choice == '1':
            image_path = input("Enter the path of the image to encrypt: ")
            key = int(input("Enter an encryption key (number): "))
            output_path = input("Enter the output path for the encrypted image: ")
            encrypt_image(image_path, key, output_path)

        elif choice == '2':
            image_path = input("Enter the path of the encrypted image: ")
            key = int(input("Enter the decryption key (number): "))
            output_path = input("Enter the output path for the decrypted image: ")
            decrypt_image(image_path, key, output_path)

        elif choice == '0':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice! Please select 1, 2, or 0.")

if __name__ == "__main__":
    main()

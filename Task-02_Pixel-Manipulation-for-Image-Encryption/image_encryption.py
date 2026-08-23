from PIL import Image
import os


def transform_image(input_file, output_file, key, decrypt=False):
    image = Image.open(input_file).convert("RGB")
    pixels = image.load()
    shift = -key if decrypt else key
    for y in range(image.height):
        for x in range(image.width):
            r, g, b = pixels[x, y]
            pixels[x, y] = ((r + shift) % 256, (g + shift) % 256, (b + shift) % 256)
    image.save(output_file)

choice = input("1. Encrypt\n2. Decrypt\nChoice: ")
input_file = input("Input image: ")
output_file = input("Output image: ")
key = int(input("Key (1-255): "))

if not os.path.exists(input_file):
    raise SystemExit("Input image not found.")
if not 1 <= key <= 255:
    raise SystemExit("Key must be between 1 and 255.")
if choice not in ("1", "2"):
    raise SystemExit("Invalid choice.")

transform_image(input_file, output_file, key, decrypt=(choice == "2"))
print("Done:", output_file)

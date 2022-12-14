# Requires PIL Library.
from io import BytesIO
from PIL import Image

# Points to image. Replace with correct file path.
with open("C:\\Users\\User\\Downloads\\A-Cat-Picture.png", "rb") as f:
    data = f.read()

# Creates image data.
image = Image.open(BytesIO(data)).convert("RGBA")

width, height = image.size

aspect_ratio = width / height

# Resize to fit. Aspect ratio can be changed below.
image = image.resize((200, int(100/ aspect_ratio)), resample=Image.BICUBIC)

width, height = image.size

pixels = [
    image.getpixel((x, y))
    for y in range(height)
    for x in range(width)
    if image.getpixel((x, y))[3] != 0
]

# List of ASCII Characters.
ASCII_CHARS = [" ","Z","Y","X","W","V","U","T","S","R","Q","P","N","M","L","K","J","I","H","G","F","E","C","A","#","&","$","%","@"]

# Reversed list.
ASCII_CHARS = list(reversed(ASCII_CHARS))

# Required for Transparency.
darkest_char = ASCII_CHARS.pop()

# Opens a text file for the output.
with open("output.txt", "w") as f:
    for y in range(height):
        for x in range(width):
            pixel = image.getpixel((x, y))
            # Check for transparency and writes a space for formatting.
            if pixel[3] == 0:
                f.write(" ")
                continue

            # A check for greyscale or color.
            if len(pixel) == 1:
                luminosity = pixel[0]
            else:
                luminosity = 0.21 * pixel[0] + 0.72 * pixel[1] + 0.07 * pixel[2]

            # Reversed list check.
            ASCII_CHARS = list(reversed(ASCII_CHARS))

            # ASCII Character index check.
            index = int(luminosity * (len(ASCII_CHARS) + 1) // 256)


            # Limited index to fix out of range error.
            index = min(max(index, 0), len(ASCII_CHARS) - 1)

            f.write(ASCII_CHARS[index])

        f.write("\n")

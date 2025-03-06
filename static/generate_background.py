from PIL import Image, ImageDraw
import os

# Define image size and colors
width, height = 1920, 1080  # Standard HD resolution
color_start = (230, 240, 255)  # Light blue
color_end = (200, 220, 245)    # Slightly darker blue

# Create a new image with gradient
image = Image.new('RGB', (width, height))
draw = ImageDraw.Draw(image)

# Linear gradient from top-left to bottom-right
for x in range(width):
    for y in range(height):
        r = int(color_start[0] + (color_end[0] - color_start[0]) * (x + y) / (width + height))
        g = int(color_start[1] + (color_end[1] - color_start[1]) * (x + y) / (width + height))
        b = int(color_start[2] + (color_end[2] - color_start[2]) * (x + y) / (width + height))
        draw.point((x, y), fill=(r, g, b))

# Ensure static folder exists
if not os.path.exists('static'):
    os.makedirs('static')

# Save the image
image.save('static/background.jpg', 'JPEG')
print("Background image generated as 'static/background.jpg'")
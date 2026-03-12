from PIL import Image, ImageDraw, ImageOps

def prepare_user_image(image_path, size=(350, 350)):
    img = Image.open(image_path).convert("RGBA")
    img = ImageOps.fit(img, size, centering=(0.5, 0.5))
    mask = Image.new("L", size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + size, fill=255)
    img.putalpha(mask)
    return img

from PIL import Image, ImageDraw, ImageFont
import os
from django.conf import settings

FONT_PATH = os.path.join(settings.BASE_DIR, 'fonts/SolaimanLipi.ttf')

def design_1(user_name, address, user_img):
    width, height = 1080, 1080
    image = Image.new("RGB", (width, height), (1, 50, 32))
    draw = ImageDraw.Draw(image)
    draw.rectangle([40, 40, 1040, 1040], outline="gold", width=15)
    
    font_main = ImageFont.truetype(FONT_PATH, 130)
    draw.text((width//2, 180), "ঈদ মোবারক", font=font_main, fill="gold", anchor="mm")
    
    image.paste(user_img, (365, 300), user_img)
    
    font_name = ImageFont.truetype(FONT_PATH, 75)
    draw.text((width//2, 780), user_name, font=font_name, fill="white", anchor="mm")
    
    font_addr = ImageFont.truetype(FONT_PATH, 45)
    draw.text((width//2, 870), address, font=font_addr, fill="#E0E0E0", anchor="mm")
    
    return image

def design_2(user_name, address, user_img):
    width, height = 1080, 1080
    image = Image.new("RGB", (width, height), (255, 255, 255))
    draw = ImageDraw.Draw(image)
    
    draw.rectangle([0, 0, 1080, 250], fill="#1E3A8A")
    
    font_main = ImageFont.truetype(FONT_PATH, 110)
    draw.text((width//2, 125), "EID MUBARAK", font=font_main, fill="white", anchor="mm")
    
    image.paste(user_img, (365, 350), user_img)
    
    font_name = ImageFont.truetype(FONT_PATH, 85)
    draw.text((width//2, 850), user_name, font=font_name, fill="#1E3A8A", anchor="mm")
    
    font_addr = ImageFont.truetype(FONT_PATH, 50)
    draw.text((width//2, 930), address, font=font_addr, fill="#4B5563", anchor="mm")
    
    return image

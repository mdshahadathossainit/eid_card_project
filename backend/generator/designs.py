from PIL import Image, ImageDraw, ImageFont, ImageOps
import os
from django.conf import settings

FONT_PATH = os.path.join(settings.BASE_DIR, 'fonts', 'SolaimanLipi.ttf')

def get_font(size):
    try:
        return ImageFont.truetype(FONT_PATH, size)
    except Exception as e:
        print(f"Font loading failed: {e}")
        return ImageFont.load_default()

def draw_base(img, u_img, name, addr, n_pos, a_pos, i_pos, n_clr, a_clr):
    draw = ImageDraw.Draw(img)
    img.paste(u_img, i_pos, u_img)
    draw.text(n_pos, name, font=get_font(75), fill=n_clr, anchor="mm")
    draw.text(a_pos, addr, font=get_font(45), fill=a_clr, anchor="mm")
    return img

def design_1(n, a, i):
    img = Image.new("RGB", (1080, 1080), (1, 50, 32))
    draw = ImageDraw.Draw(img)
    draw.rectangle([40, 40, 1040, 1040], outline="gold", width=15)
    draw.text((540, 180), "ঈদ মোবারক", font=get_font(130), fill="gold", anchor="mm")
    return draw_base(img, i, n, a, (540, 780), (540, 870), (365, 300), "white", "#E0E0E0")

def design_2(n, a, i):
    img = Image.new("RGB", (1080, 1080), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw.rectangle([0, 0, 1080, 250], fill="#1E3A8A")
    draw.text((540, 125), "EID MUBARAK", font=get_font(110), fill="white", anchor="mm")
    return draw_base(img, i, n, a, (540, 850), (540, 930), (365, 350), "#1E3A8A", "#4B5563")

def design_3(n, a, i):
    img = Image.new("RGB", (1080, 1080), "#5D4037")
    draw = ImageDraw.Draw(img)
    draw.text((540, 150), "সবাইকে ঈদের শুভেচ্ছা", font=get_font(90), fill="#FFCCBC", anchor="mm")
    return draw_base(img, i, n, a, (540, 820), (540, 900), (365, 300), "white", "#D7CCC8")

def design_4(n, a, i):
    img = Image.new("RGB", (1080, 1080), "#004D40")
    draw = ImageDraw.Draw(img)
    draw.ellipse([340, 240, 740, 640], outline="#80CBC4", width=10)
    return draw_base(img, i, n, a, (540, 800), (540, 880), (365, 265), "#B2DFDB", "white")

def design_5(n, a, i):
    img = Image.new("RGB", (1080, 1080), "#1A237E")
    draw = ImageDraw.Draw(img)
    draw.line([(0, 540), (1080, 540)], fill="#3F51B5", width=400)
    return draw_base(img, i, n, a, (540, 850), (540, 930), (365, 300), "#C5CAE9", "white")

def design_6(n, a, i):
    img = Image.new("RGB", (1080, 1080), "#BF360C")
    draw = ImageDraw.Draw(img)
    draw.rectangle([50, 50, 1030, 1030], outline="white", width=5)
    return draw_base(img, i, n, a, (540, 820), (540, 900), (365, 320), "white", "#FFCCBC")

def design_7(n, a, i):
    img = Image.new("RGB", (1080, 1080), "#311B92")
    draw = ImageDraw.Draw(img)
    draw.text((540, 540), "EID", font=get_font(450), fill="#4527A0", anchor="mm")
    return draw_base(img, i, n, a, (540, 880), (540, 950), (365, 250), "white", "#D1C4E9")

def design_8(n, a, i):
    img = Image.new("RGB", (1080, 1080), "#F57F17")
    draw = ImageDraw.Draw(img)
    draw.rectangle([0, 0, 1080, 1080], outline="#FFF9C4", width=30)
    return draw_base(img, i, n, a, (540, 800), (540, 880), (365, 300), "black", "#3E2723")

def design_9(n, a, i):
    img = Image.new("RGB", (1080, 1080), "#E91E63")
    draw = ImageDraw.Draw(img)
    draw.polygon([(540, 20), (1060, 540), (540, 1060), (20, 540)], outline="white", width=10)
    return draw_base(img, i, n, a, (540, 820), (540, 900), (365, 300), "white", "#FCE4EC")

def design_10(n, a, i):
    img = Image.new("RGB", (1080, 1080), "black")
    draw = ImageDraw.Draw(img)
    draw.text((540, 150), "عيد مبارك", font=get_font(160), fill="gold", anchor="mm")
    return draw_base(img, i, n, a, (540, 800), (540, 880), (365, 300), "gold", "white")

def design_11(n, a, i):
    img = Image.new("RGB", (1080, 1080), "#01579B")
    draw = ImageDraw.Draw(img)
    draw.rectangle([0, 800, 1080, 1080], fill="#0288D1")
    return draw_base(img, i, n, a, (540, 900), (540, 980), (365, 250), "white", "#E1F5FE")

def design_12(n, a, i):
    img = Image.new("RGB", (1080, 1080), "#263238")
    draw = ImageDraw.Draw(img)
    draw.rectangle([100, 100, 980, 200], fill="#CFD8DC")
    return draw_base(img, i, n, a, (540, 850), (540, 930), (365, 350), "#ECEFF1", "#90A4AE")

def design_13(n, a, i):
    img = Image.new("RGB", (1080, 1080), "#FFD600")
    draw = ImageDraw.Draw(img)
    draw.ellipse([-100, -100, 400, 400], fill="#FBC02D")
    return draw_base(img, i, n, a, (540, 820), (540, 900), (365, 300), "black", "#424242")

def design_14(n, a, i):
    img = Image.new("RGB", (1080, 1080), "#880E4F")
    draw = ImageDraw.Draw(img)
    draw.line([(0, 0), (1080, 1080)], fill="#AD1457", width=50)
    return draw_base(img, i, n, a, (540, 850), (540, 930), (365, 250), "white", "#F8BBD0")

def design_15(n, a, i):
    img = Image.new("RGB", (1080, 1080), "#1B5E20")
    draw = ImageDraw.Draw(img)
    draw.rectangle([40, 40, 1040, 1040], outline="#A5D6A7", width=5)
    return draw_base(img, i, n, a, (540, 800), (540, 880), (365, 300), "white", "#C8E6C9")

def design_16(n, a, i):
    img = Image.new("RGB", (1080, 1080), "#212121")
    draw = ImageDraw.Draw(img)
    draw.text((540, 540), "MUBARAK", font=get_font(200), fill="#323232", anchor="mm")
    return draw_base(img, i, n, a, (540, 850), (540, 930), (365, 300), "gold", "#BDBDBD")

def design_17(n, a, i):
    img = Image.new("RGB", (1080, 1080), "#F5F5F5")
    draw = ImageDraw.Draw(img)
    draw.rectangle([0, 0, 1080, 300], fill="#00C853")
    return draw_base(img, i, n, a, (540, 850), (540, 930), (365, 380), "#1B5E20", "#757575")

def design_18(n, a, i):
    img = Image.new("RGB", (1080, 1080), "#006064")
    draw = ImageDraw.Draw(img)
    draw.ellipse([200, 200, 880, 880], outline="#00ACC1", width=2)
    return draw_base(img, i, n, a, (540, 920), (540, 1000), (365, 320), "white", "#B2EBF2")

def design_19(n, a, i):
    img = Image.new("RGB", (1080, 1080), "#4A148C")
    draw = ImageDraw.Draw(img)
    draw.rectangle([540, 0, 1080, 1080], fill="#6A1B9A")
    return draw_base(img, i, n, a, (540, 850), (540, 930), (365, 300), "white", "#E1BEE7")

def design_20(n, a, i):
    img = Image.new("RGB", (1080, 1080), "#DD2C00")
    draw = ImageDraw.Draw(img)
    draw.text((540, 100), "EID 2026", font=get_font(120), fill="white", anchor="mm")
    return draw_base(img, i, n, a, (540, 850), (540, 930), (365, 300), "white", "#FF9E80")

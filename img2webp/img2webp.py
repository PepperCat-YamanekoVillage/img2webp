import glob
from PIL import Image

img_format_list = ['*.png','*.PNG','*.jpg','*.jpeg','*.JPEG']
img_list = []

for img_format in img_format_list:
    img_list += glob.glob(img_format)

for img in img_list:
    webp = Image.open(img)
    img_name = img.split(".")[0]
    webp.save(img_name + ".webp",format = "WebP")
    large_webp = webp.resize((1200,630))
    large_webp.save(img_name + "-large.webp",format = "WebP")
    small_webp = webp.resize((412,216))
    small_webp.save(img_name + "-small.webp",format = "WebP")

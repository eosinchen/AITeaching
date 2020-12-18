from PIL import Image
import os

# 轉 jpg
for img in os.listdir("./images"):
    if img.endswith(".png"):
        im = Image.open("./images/{}".format(img))
        rgb_im = im.convert("RGB")
        img_name = img.split(".")[0]
        rgb_im.save("./images/{}.jpg".format(img_name))
        print("./images/{}.jpg".format(img_name))

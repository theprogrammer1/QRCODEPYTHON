from PIL import Image, ImageDraw
import qrcode
data="hello"
image = qrcode.make(data)
image.save("abc1231.png")
# install the module like this pip install pillow qrcode

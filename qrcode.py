import pyqrcode
# enter what text you want or a web address.
qr = pyqrcode.create('www.google.com')
qr.png('abc1.png', scale=8)
# You can then scan this with your phone.

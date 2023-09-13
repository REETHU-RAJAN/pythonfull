import pyqrcode
from pyqrcode import QRCode
message="hi dears"
url=pyqrcode.create(message)
url.svg("myprcode.svg",scale=8)

import qrcode as qr

myqr = qr.make("https://www.youtube.com/")
myqr.save("myqr.png")
import qrcode as qr 
img = qr.make("https://www.google.com/?hl=chrome")
img.save("googleqr.png")
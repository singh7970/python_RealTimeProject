import qrcode as qr

# h=qr.make("HELLO akanksha kesi ho  sab thik na ")
# h.save("QRcode/web.png")



import qrcode as qr
with open('QRcode/basic.html','r') as file:
    txt=file.read()

img=qr.make(txt)
img.save('txt.png')
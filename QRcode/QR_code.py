import qrcode as qr

h=qr.make("https://django-project-xdtk.onrender.com/")
h.save("QRcode/web.png")



# import qrcode as qr
# with open('QRcode/basic.html','r') as file:
#     txt=file.read()

# img=qr.make(txt)
# img.save('txt.png')
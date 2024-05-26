# import qrcode as qr
# img=qr.make("")
# img.save("hello.png")





# to pass a html file
import qrcode as qr
with open('QRcode/basic_info.txt','r') as file:
   info=file.read()
   img=qr.make(info)
   img.save('QRcode/dhoni.png')
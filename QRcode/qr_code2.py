import qrcode as qr

# t=qr.make("hi my name is priyanshi singh")
# t.save("QRcode/asg.jpg")

with open('QRcode/basic.html','r') as f:
    t=f.read()

    
j=qr.make(t)
j.save("QRcode/djb.png")    
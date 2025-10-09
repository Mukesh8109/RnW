import qrcode
data = "QR"
qr = qrcode.make(data)
qr.save("qr.png")
print("qr code or what")

import qrcode
url="http://localhost:5000/report"
qr=qrcode.make(url)
qr.save("qrcode.png")